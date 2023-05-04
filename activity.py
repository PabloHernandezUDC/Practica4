# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es

class Activity():
    '''
    '''
    def __init__(self, name, duration, participants, cost):
        '''
        '''
        self._name = name
        try:
            self._duration = float(duration)
        except ValueError:
            self._duration = duration
        try:
            self._participants = float(participants)
        except ValueError:
            self._participants = participants
        try:
            self._cost = float(cost)
        except ValueError:
            self._cost = cost
    
    def __lt__(self, other):
        '''
        '''
        return self.get_total_needed_resources() < other.get_total_needed_resources()
    
    def get_total_needed_resources(self):
        '''
        '''
        return self._cost/self._participants/(self._duration/60)
            
    def get_name(self):
        '''
        '''
        return self._name
    
    def set_name(self, input_name):
        '''
        '''
        self._name = input_name

    def get_duration(self):
        '''
        '''
        return self._duration
    
    def set_duration(self, input_duration):
        '''
        '''
        self._duration = input_duration

    def get_participants(self):
        '''
        '''
        return self._participants
    
    def set_participants(self, input_participants):
        '''
        '''
        self._participants = input_participants

    def get_cost(self):
        '''
        '''
        return self._cost
    
    def set_cost(self, input_cost):
        '''
        '''
        self._cost = input_cost