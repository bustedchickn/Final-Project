from game.action import Action

# TODO: Define the DrawActorsAction class here
class DrawActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._output_service = output_service
        

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        
        marquee = cast["marquee"][0]
        self._output_service.draw_actor(marquee)

        



        
        artifacts = cast["artifact"]
        self._output_service.draw_actors(artifacts)

        robot = cast["robot"][0]
        self._output_service.draw_actor(robot)



        self._output_service.flush_buffer()