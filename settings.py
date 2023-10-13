class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bullets_allowed = 3

        # Ship settings
        self.ship_speed = 4.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Alien Settings
        self.alien_speed = 20.0
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
