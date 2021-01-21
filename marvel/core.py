from abc import ABC
from .alliance import Alliance

IDENTIFIER = 3249832743924

class CompositeMetaClass(type(commands.Cog), type(ABC)):
    pass
    
class Marvel(Alliance, commands.Cog, metaclass=CompositeMetaClass):
    """Marvel commands built for WALL-E."""
    
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self, 
            IDENTIFIER, 
            force_registration=True
        )
        self.config.register_guild(
            timezone=None, 
            officerrole=None
        )
        self.config.register_user(
            tzon=False
        )
