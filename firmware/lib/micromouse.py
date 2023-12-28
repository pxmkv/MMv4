
import machine





class Mice(object):
    led = machine.Pin(0)
    """Motor and PWM"""
    Left_Motor_Pin  = machine.Pin(1)
    Right_Motor_Pin = machine.Pin(2)
    Left_Motor  = machine.PWM(Left_Motor_Pin)
    Right_Motor = machine.PWM(Right_Motor_Pin)

    def __init__(self,pwm_freq=20000):
        self.Left_Motor.freq(pwm_freq)
        self.Right_Motor.freq(pwm_freq)
        return 
    def motor(Left,Right):
        Left_Motor.duty(Left)
        Right_Motor.duty(Right)


 