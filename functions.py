def getExtraversionScore(df):
    """To Calcualte the Extraversion Score"""
    ExtraversionScore = 0
    ExtraversionScore = 20 + df['EXT1'] - df['EXT2'] + df['EXT3'] - df['EXT4'] + df['EXT5'] - df['EXT6'] + df['EXT7'] - df['EXT8'] + df['EXT9'] - df['EXT10']
    return ExtraversionScore

def getAgreeablenessScore(df):
    """To Calcualte the Agreeableness Score"""
    AgreeablenessScore = 0
    AgreeablenessScore = 14 - df['AGR1'] + df['AGR2'] - df['AGR3'] + df['AGR4'] - df['AGR5'] + df['AGR6'] - df['AGR7'] + df['AGR8'] + df['AGR9'] + df['AGR10']
    return AgreeablenessScore

def getConscientiousnessScore(df):
    """To Calcualte the Conscientiousness Score"""
    ConscientiousnessScore = 0
    ConscientiousnessScore = 14 + df['CSN1'] - df['CSN2'] + df['CSN3'] - df['CSN4'] + df['CSN5'] - df['CSN6'] + df['CSN7'] - df['CSN8'] + df['CSN9'] + df['CSN10']
    return ConscientiousnessScore

def getEmotionalStabilityScore(df):
    """To Calcualte the EmotionalStability Score"""
    EmotionalStabilityScore = 0
    EmotionalStabilityScore = 38 - df['EST1'] + df['EST2'] - df['EST3'] + df['EST4'] - df['EST5'] - df['EST6'] - df['EST7'] - df['EST8'] - df['EST9'] - df['EST10']
    return EmotionalStabilityScore

def getOpennessScore(df):
    """To Calcualte the Openness Score"""
    OpennessScore = 0
    OpennessScore = 8 + df['OPN1'] - df['OPN2'] + df['OPN3'] - df['OPN4'] + df['OPN5'] - df['OPN6'] + df['OPN7'] + df['OPN8'] + df['OPN9'] + df['OPN10']
    return OpennessScore