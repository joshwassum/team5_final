import arcade
from game import constants


class PlayerSpriteAnimation(arcade.Sprite):
    """A code template for moving actors. The responsibility of this class of
        objects load the animation images in pairs for the player sprite.

        The data is returned as the Player_sprite object in the scene.

        Stereotype:
            Actor
  
    """

    def __init__(self):
        """The class constructor

        Args:
            self.character_face_direction (int): sets the default facing direction
            self.current_texture (int): sets the defualt image
            self.scale (int): sets the scale for the player sprite

            self.jumping (bool): Used to identify player state
            self.climbing (bool): Used to identify player state
            self.is_on_ladder (bool): Used to identify player state
        """
        super().__init__()

        self.character_face_direction = constants.RIGHT_FACING
        self.current_texture = 0
        self.scale = constants.CHARACTER_SCALE
        self.jumping = False
        self.climbing = False
        self.is_on_ladder = False
        self._physics_engine = None

        self._setup()

    def _setup(self):
        """The conpletes class construction. Loads all the images required for animating the player sprite.

        Args:
            self.idle_texture_pair (list): loads copy of original image and a mirrored copy
            self.jump_texture_pair (list): loads copy of original image and a mirrored copy
            self.fall_texture_pair (list): loads copy of original image and a mirrored copy
            self.walk_textures (list): loads copy of original images and a mirrored copys for all 9 walking images in order
            self.climbing_textures (list): loads copy of original image and a mirrored copy
        """


        self.idle_texture_pair = self.load_picture_pairs(f"{constants.MAIN_FILE}_idle.png")
        self.jump_texture_pair = self.load_picture_pairs(f"{constants.MAIN_FILE}_jump.png")
        self.fall_texture_pair = self.load_picture_pairs(f"{constants.MAIN_FILE}_fall.png")

        self.walk_textures = []
        for i in range(8):
            texture = self.load_picture_pairs(f"{constants.MAIN_FILE}_walk{i}.png")
            self.walk_textures.append(texture)

        self.climbing_textures = []
        texture = arcade.load_texture(f"{constants.MAIN_FILE}_climb0.png")
        self.climbing_textures.append(texture)
        texture = arcade.load_texture(f"{constants.MAIN_FILE}_climb1.png")
        self.climbing_textures.append(texture)

        self.texture = self.idle_texture_pair[0]

    def load_picture_pairs(self, filename):
        """
        Load the picture pairs, with the second being a mirror image.

        Args:
            filename (str): sets the default file location

        """
        return [
            arcade.load_texture(filename),
            arcade.load_texture(filename, flipped_horizontally=True),
        ]


    def update_animation(self, delta_time: float = 1 / 60):
        """
        Game logic to determine player animation and direction.

        Args:
            self.character_face_direction (int): tracks the player movement direction
            
        
        """

        if self.change_x < 0 and self.character_face_direction == constants.RIGHT_FACING:
            self.character_face_direction = constants.LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == constants.LEFT_FACING:
            self.character_face_direction = constants.RIGHT_FACING

        # Sets up player climbing animation
        if self.is_on_ladder:
            self.climbing = True
        if not self.is_on_ladder and self.climbing:
            self.climbing = False
        if self.climbing and abs(self.change_y) > 1:
            self.current_texture += 1
            if self.current_texture > 7:
                self.current_texture = 0
        if self.climbing:
            self.texture = self.climbing_textures[self.current_texture // 4]
            return

        # Jumping animation
        if self.change_y > 0 and not self.is_on_ladder:
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return
        elif self.change_y < 0 and not self.is_on_ladder:
            self.texture = self.fall_texture_pair[self.character_face_direction]
            return

        # Idle animation
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.current_texture += 1
        if self.current_texture > 7:
            self.current_texture = 0
        self.texture = self.walk_textures[self.current_texture][self.character_face_direction]