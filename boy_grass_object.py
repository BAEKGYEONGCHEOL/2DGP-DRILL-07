from pico2d import *
import random


# Game object class here
class Grass:
    # 생성자함수 초기화수행
    def __init__(self):
        # grass 객체의 속성을 정의하고 초기화
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)    # grass 그리기
        pass

    def update(self):
        pass

class Boy:
    # 생성자함수 초기화수행
    def __init__(self):
    # boy 객체의 속성을 정의하고 초기화
        self.image = load_image('run_animation.png')
        self.x = random.randint(100, 700)     # boy 의 x 좌표(랜덤하게 시작)
        self.frame = random.randint(1, 7)     # boy 의 애니메이션 프레임(랜덤하게 시작)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 90)     # boy 그리기
        pass

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8
        pass

    pass

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height, self.x, self.y, frame_width // 2, frame_height // 2)

class SmallBall:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = 599
        self.speed = random.randint(3, 10)
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y - self.speed > 60:
            self.y -= self.speed
        else:
            self.y = 60

    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y, 21, 21)
    pass

class BigBall:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = 599
        self.speed = random.randint(3, 10)
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y - self.speed > 70:
            self.y -= self.speed
        else:
            self.y = 70

    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y, 41, 41)
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()


def reset_world():
    global running
    global world    # world list = 모든 객체들을 갖고 있는 리스트

    world = []  # 하나도 객체가 없는 world
    running = True

    # grass 를 만들고 world 에 추가
    grass = Grass()
    world.append(grass)

    # team 을 만들고 world 에 추가
    team = [Boy() for _ in range(11)]
    world += team   # 리스트이기 때문에 += 연산자 사용

    # zombie 를 만들고 world 에 추가
    zombie = Zombie()
    world.append(zombie)

    # smallBalls 를 만들고 world 에 추가
    smallBalls = [SmallBall() for _ in range(10)]
    world += smallBalls

    # bigBalls 를 만들고 world 에 추가
    bigBalls = [BigBall() for _ in range(10)]
    world += bigBalls

    pass

# 게임 로직
def update_world():
    for game_object in world:
        game_object.update()
    # grass.update()  # grass 객체를 다시 그릴 필요는 없지만 사용할 때가 올 수도 있기 때문에 만들어 두는 것이 좋다.
    # for boy in team:
    #     boy.update()  # boy 의 상호작용을 시뮬레이션 계산
    pass

def render_world():
    # 월드의 객체들을 그린다.
    clear_canvas()
    for game_object in world:
        game_object.draw()
    # grass.draw()
    # for boy in team:
    #     boy.draw()
    update_canvas()
    pass


reset_world()

# 게임 루프
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
