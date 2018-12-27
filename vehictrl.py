import RPi.GPIO as GPIO


MOTOR_LF_IN1 = 5
MOTOR_LF_IN2 = 6
MOTOR_LB_IN1 = 13
MOTOR_LB_IN2 = 19
MOTOR_RF_IN1 = 12
MOTOR_RF_IN2 = 16
MOTOR_RB_IN1 = 20
MOTOR_RB_IN2 = 21


def init(mlf1 = 5, mlf2 = 6, mlb1 = 13, mlb2 = 19, mrf1 = 12, mrf2 = 16, mrb1 = 20, mrb2 = 21):
    GPIO.setmode(GPIO.BCM)

    MOTOR_LF_IN1 = mlf1
    MOTOR_LF_IN2 = mlf2
    MOTOR_LB_IN1 = mlb1
    MOTOR_LB_IN2 = mlb2
    MOTOR_RF_IN1 = mrf1
    MOTOR_RF_IN2 = mrf2
    MOTOR_RB_IN1 = mrb1
    MOTOR_RB_IN2 = mrb2

    GPIO.setup(MOTOR_LF_IN1, GPIO.OUT)
    GPIO.setup(MOTOR_LF_IN2, GPIO.OUT)
    GPIO.setup(MOTOR_LB_IN1, GPIO.OUT)
    GPIO.setup(MOTOR_LB_IN2, GPIO.OUT)
    GPIO.setup(MOTOR_RF_IN1, GPIO.OUT)
    GPIO.setup(MOTOR_RF_IN2, GPIO.OUT)
    GPIO.setup(MOTOR_RB_IN1, GPIO.OUT)
    GPIO.setup(MOTOR_RB_IN2, GPIO.OUT)
    pass

def release():
    GPIO.cleanup()
    pass

def moveFore():
    GPIO.output(MOTOR_LF_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_LF_IN2, GPIO.LOW)
    GPIO.output(MOTOR_LB_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_LB_IN2, GPIO.LOW)
    GPIO.output(MOTOR_RF_IN1, GPIO.LOW)
    GPIO.output(MOTOR_RF_IN2, GPIO.HIGH)
    GPIO.output(MOTOR_RB_IN1, GPIO.LOW)
    GPIO.output(MOTOR_RB_IN2, GPIO.HIGH)
    pass
    
def moveBack():
    GPIO.output(MOTOR_LF_IN1, GPIO.LOW)
    GPIO.output(MOTOR_LF_IN2, GPIO.HIGH)
    GPIO.output(MOTOR_LB_IN1, GPIO.LOW)
    GPIO.output(MOTOR_LB_IN2, GPIO.HIGH)
    GPIO.output(MOTOR_RF_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_RF_IN2, GPIO.LOW)
    GPIO.output(MOTOR_RB_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_RB_IN2, GPIO.LOW)
    pass
    
def moveLeft():
    GPIO.output(MOTOR_LF_IN1, GPIO.LOW)
    GPIO.output(MOTOR_LF_IN2, GPIO.HIGH)
    GPIO.output(MOTOR_LB_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_LB_IN2, GPIO.LOW)
    GPIO.output(MOTOR_RF_IN1, GPIO.LOW)
    GPIO.output(MOTOR_RF_IN2, GPIO.HIGH)
    GPIO.output(MOTOR_RB_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_RB_IN2, GPIO.LOW)
    pass
    
def moveRight():
    GPIO.output(MOTOR_LF_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_LF_IN2, GPIO.LOW)
    GPIO.output(MOTOR_LB_IN1, GPIO.LOW)
    GPIO.output(MOTOR_LB_IN2, GPIO.HIGH)
    GPIO.output(MOTOR_RF_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_RF_IN2, GPIO.LOW)
    GPIO.output(MOTOR_RB_IN1, GPIO.LOW)
    GPIO.output(MOTOR_RB_IN2, GPIO.HIGH)
    pass

def turnLeft():
    GPIO.output(MOTOR_LF_IN1, GPIO.LOW)
    GPIO.output(MOTOR_LF_IN2, GPIO.HIGH)
    GPIO.output(MOTOR_LB_IN1, GPIO.LOW)
    GPIO.output(MOTOR_LB_IN2, GPIO.HIGH)
    GPIO.output(MOTOR_RF_IN1, GPIO.LOW)
    GPIO.output(MOTOR_RF_IN2, GPIO.HIGH)
    GPIO.output(MOTOR_RB_IN1, GPIO.LOW)
    GPIO.output(MOTOR_RB_IN2, GPIO.HIGH)
    pass

def turnRight():
    GPIO.output(MOTOR_LF_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_LF_IN2, GPIO.LOW)
    GPIO.output(MOTOR_LB_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_LB_IN2, GPIO.LOW)
    GPIO.output(MOTOR_RF_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_RF_IN2, GPIO.LOW)
    GPIO.output(MOTOR_RB_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_RB_IN2, GPIO.LOW)
    pass

def stop():
    GPIO.output(MOTOR_LF_IN1, GPIO.LOW)
    GPIO.output(MOTOR_LF_IN2, GPIO.LOW)
    GPIO.output(MOTOR_LB_IN1, GPIO.LOW)
    GPIO.output(MOTOR_LB_IN2, GPIO.LOW)
    GPIO.output(MOTOR_RF_IN1, GPIO.LOW)
    GPIO.output(MOTOR_RF_IN2, GPIO.LOW)
    GPIO.output(MOTOR_RB_IN1, GPIO.LOW)
    GPIO.output(MOTOR_RB_IN2, GPIO.LOW)
    pass