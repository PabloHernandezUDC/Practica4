# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es

class Activity():
    '''
    Class that represents an activity that can have a name, duration, number of participants, and cost.

    Attributes
    ----------
    name : str
        The name of the activity.
    duration : float
        Duration in minutes of said activity.
    participants : float
        Number of people particpating in the activity.
    cost: float
        Monetary cost of the activity.
    
    Methods
    -------
    __lt__(self, other):
        Overriding the magic method for < so that activities are sorted according to their total cost.
    
    get_total_needed_resources(self):
        Calculates total cost for an activity based on the current values of some of its attributes.
        (cost / participants / duration in hours)

    Getters and setters for all attributes.   
    '''
    
    def __init__(self, name, duration, participants, cost):
        '''
        Initializes the activity attributes with the values provided as arguments.

        Parameters
        --------------
        name str: The name of the activity.
        duration float: The duration of the activity.
        participants float: The number of participants in the activity.
        cost float: The cost of the activity.
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
        Compares two activities and determines which requires fewer resources.

        Parameters
        ----------
            other (Activity): The other activity to compare with.

        Returns
        ----------
            bool: True if this activity requires fewer resources than the other, false otherwise.
        '''
        return self.get_total_needed_resources() < other.get_total_needed_resources()
    
    def get_total_needed_resources(self):
        '''
        Calculates the amount of resources needed to carry out the activity.

        Returns
        -----------
            float: The amount of resources needed, which is defined as the cost divided by the number of participants and duration in hours.
        '''
        return self._cost/self._participants/(self._duration/60)
            
    def get_name(self):
        '''
        Returns the name of the activity.

        Returns
        --------
            str: The name of the activity.

        '''
        return self._name
    
    def set_name(self, input_name):
        '''
        Sets the name of the activity to the given input.

       Parameters
       -------------
            input_name (str): The new name of the activity.

        '''
        self._name = input_name

    def get_duration(self):
        '''
        Returns the duration of the activity.

        Returns
        -----------
            float: The duration of the activity.
        '''
        return self._duration
    
    def set_duration(self, input_duration):
        '''
        Sets the duration of the activity to the given input.

        Parameters
        ----------
            input_duration float: The new duration for the activity.
        
        '''
        self._duration = input_duration

    def get_participants(self):
        '''
        Returns the number of participants in the activity.

        Returns
        ---------
            float: The number of participants in the activity.
        
        '''
        return self._participants
    
    def set_participants(self, input_participants):
        '''
        Sets the number of participants in the activity to the given input.

        Parameters
        -----------
            input_participants float: The new number of participants for the activity.
        '''
        self._participants = input_participants

    def get_cost(self):
        '''
        Returns the cost of the activity.

        Returns
        ----------
            float: The cost of the activity.
        '''
        return self._cost
    
    def set_cost(self, input_cost):
        '''
        Sets the number of participants in the activity to the given input.

        Parameters
        -----------
            input_cost float: The new cost for the activity.
        '''
        self._cost = input_cost