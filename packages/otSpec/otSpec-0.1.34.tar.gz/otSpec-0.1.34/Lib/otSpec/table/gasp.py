'''Constants related to gasp table defined by Opentype spec.

source: http://www.microsoft.com/typography/otspec/gasp.htm
'''
# gasp Behavior
GRIDFIT             = 1
DOGRAY              = 2
SYMMETRIC_GRIDFIT   = 4
SYMMETRIC_SMOOTHING = 8

# valid gasp Behavior for gasp table version 0
validGaspBehavior_v0 = DOGRAY|GRIDFIT

# valid gasp Behavior for gasp table version 1
validGaspBehavior_v1 = validGaspBehavior_v0|SYMMETRIC_GRIDFIT|SYMMETRIC_SMOOTHING