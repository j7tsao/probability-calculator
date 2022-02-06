import random
import copy

class Hat:
    
    def __init__(self, **balls):
        self.contents = list()
        # balls are passed in as a dict
        self.balls = balls
        # convert self.balls from a dict to a list named self.contents
        for item in balls:
            for i in range(balls.get(item)):
                self.contents.append(item)

    def draw(self, num2draw):
        if num2draw >= len(self.contents):
            return self.contents
        else:
            ballsDrawn = random.sample(list(enumerate(self.contents)), num2draw)
            newContents = list()
            ballsDrawn_list = list()
            for id, ball in ballsDrawn:
                ballsDrawn_list.append(ball)
            for id, ball in list(enumerate(self.contents)):
                if not (id, ball) in ballsDrawn:
                    newContents.append(ball)
            self.contents = newContents
            return ballsDrawn_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    allMatchedCount = 0
    num_cycle = num_experiments
    contents = copy.deepcopy(hat.contents)
    while num_cycle > 0:
        hat.contents = copy.deepcopy(contents)
        ballsDrawn = hat.draw(num_balls_drawn)
        ballsDrawn_dict = dict()

        # convert  
        for i in ballsDrawn:
            ballsDrawn_dict[i] = ballsDrawn_dict.get(i, 0) + 1

        # Check if expected balls got drawn
        elem_matchCount = 0
        for ball in expected_balls:
            if ball in ballsDrawn_dict and ballsDrawn_dict[ball] >= expected_balls[ball]:
                elem_matchCount += 1
        if elem_matchCount == len(expected_balls):
            allMatchedCount += 1
        num_cycle -= 1
    
    return allMatchedCount / num_experiments

# instantiation and testing
hat = Hat(red=5,blue=2)

probability = experiment(hat, 
                  expected_balls={"red":2,"blue":1},
                  num_balls_drawn=2,
                  num_experiments=2000)

# print(hat1.balls)
# print(type(hat1.balls))
print(hat.contents)
print(hat.draw(5))
print(probability)