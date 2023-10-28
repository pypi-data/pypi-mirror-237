import threading

class TransferController:
    def __init__(self, id_generator):
        self.request_states = {}
        self.sequence_counter = 0
        self.global_lock = threading.Lock()
        self.get_unique_id_lock = threading.Lock()
        self.id_generator = id_generator

    def _get_unique_id(self):
        with self.get_unique_id_lock:
            return next(self.id_generator)

    def _submit_sequence(self, sequence=None, on_ready=None, wait_for=None):
        sequence_id = self.sequence_counter
        self.sequence_counter += 1

        request_state = {
            'current_index': 0,
            'transfer_ids': [],
            'responses': [],
            'sequence': sequence,
            'on_ready': on_ready,
            'complete_event': threading.Event(),
            'sequence_id': sequence_id,
        }

        self.request_states[sequence_id] = request_state

        for _ in range(len(sequence)):
            unique_transfer_id = self._get_unique_id()
            request_state['transfer_ids'].append(unique_transfer_id)

        def sequence_runner():
            if wait_for is not None:
                self.wait_for(wait_for)

            current_index = request_state['current_index']
            func = sequence[current_index]
            with self.global_lock:
                func(request_state['transfer_ids'][current_index])

        thread = threading.Thread(target=sequence_runner, daemon=True)
        thread.start()

        return sequence_id

    def submit(self, *args, sequence=None, on_ready=None, wait_for=None):
        if sequence is None and len(args) == 1 and callable(args[0]):
            # Single function submitted
            func = args[0]
            return self._submit_sequence([func], on_ready or on_ready, wait_for)
        elif sequence:
            # Sequence of functions submitted
            return self._submit_sequence(sequence, on_ready, wait_for)

    def wait_for(self, sequence_id):
        if sequence_id in self.request_states:
            self.request_states[sequence_id]['complete_event'].wait()

    def wait_for_all(self):
        for sequence_id in self.request_states:
            self.request_states[sequence_id]['complete_event'].wait()

    def handle_response(self, *, transfer_id, response):
        # Get the sequence id
        sequence_id = None
        for seq_id, state in self.request_states.items():
            if not state['complete_event'].is_set() and transfer_id in state['transfer_ids']:
                sequence_id = seq_id
                break

        if sequence_id is None:
            return False

        request_state = self.request_states[sequence_id]
        current_index = request_state['current_index']

        if transfer_id == request_state['transfer_ids'][current_index]:
            request_state['responses'].append(response)
            current_index += 1
            request_state['current_index'] = current_index

            if current_index < len(request_state['sequence']):
                func = request_state['sequence'][current_index]
                with self.global_lock:
                    func(request_state['transfer_ids'][current_index])
            else:
                if request_state['on_ready']:
                    request_state['on_ready'](request_state['responses'])
                request_state['complete_event'].set()

        return True
