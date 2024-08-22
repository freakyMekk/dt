import time
import sys

global Western
global Chinese
global Running

Western = False
Chinese = False
Running = True
def western():
    Western = True
    while Western == True:
        day = int(input("Input birthday: "))

        month = input("Input month of birth (e.g. march, july etc): ")

        if month == 'december':
            astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
            if astro_sign == 'Sagittarius':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Sagittarians are adventurous and optimistic. Their love for freedom and exploration drives them to seek new experiences and knowledge.")
                print("Weaknesses:  However, Sagittarians can be blunt and impatient. Their quest for adventure may lead to restlessness and lack of commitment")
                print("Your symbol is:  Archer")
                print("Your lucky number is:  6")
                print("Your planet / star is:  Jupiter")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Capricorn':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Capricorns are disciplined and responsible. Their ambition and practicality ensure they achieve their goals and maintain sustainability.")
                print("Weaknesses:  Yet, capricorns can be pessimistic and overly cautious. Their focus on success may lead to workaholism and emotional restraint.")
                print("Your symbol is:  Goat")
                print("Your lucky number is:  4")
                print("Your planet / star is:  Saturn")
                print(" ")
                time.sleep(3)
                Western = False
        elif month == 'january':
            astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
            if astro_sign == 'Aquarius':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Aqurious are innovative and independent. Their humanitarian outlook and originality inspire progressive change and new ideas.")
                print("Weaknesses:  On the downside, Aquarians can be aloof and unpredictable. Their detachment may lead to emotional unavailability and eccentricity.")
                print("Your symbol is:  Water Carrier")
                print("Your lucky number is:  22")
                print("Your planet / star is:  Uranus")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Capricorn':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Capricorns are disciplined and responsible. Their ambition and practicality ensure they achieve their goals and maintain sustainability.")
                print("Weaknesses:  Yet, capricorns can be pessimistic and overly cautious. Their focus on success may lead to workaholism and emotional restraint.")
                print("Your symbol is:  Goat")
                print("Your lucky number is:  4")
                print("Your planet / star is:  Saturn")
                print(" ")
                time.sleep(3)
                Western = False
        elif month == 'february':
            astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
            if astro_sign == 'Aquarius':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Aqurious are innovative and independent. Their humanitarian outlook and originality inspire progressive change and new ideas.")
                print("Weaknesses:  On the downside, Aquarians can be aloof and unpredictable. Their detachment may lead to emotional unavailability and eccentricity.")
                print("Your symbol is:  Water Carrier")
                print("Your lucky number is:  22")
                print("Your planet / star is:  Uranus")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Pisces':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Pisces are compassionate and artistic. Their empathy and creativity allows them to connect deeply with others and express themselves uniquely.")
                print("Weaknesses:  Conversely, Pisces can be overly idealistic and escapist. Their sensetivity may lead to vulnerability and avoidance of reality.")
                print("Your symbol is:  Fish")
                print("Your lucky number is:  11")
                print("Your planet / star is:  Neptune")
                print(" ")
                time.sleep(3)
                Western = False
        elif month == 'march':
            astro_sign = 'Pisces' if (day < 21) else 'Aries'
            if astro_sign == 'Aries':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Aries are known for their courage and determination. Their leadership skills are unmatched, and they tackle challenges head-on with an infectious enthusiasm.")
                print("Weaknesses:  However, they can be impulsive and quick-tempered. Their competitive nature sometimes leads to impatience and conflicts.")
                print("Your symbol is:  Ram")
                print("Your lucky number is:  5")
                print("Your planet / star is:  Mars")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Pisces':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Pisces are compassionate and artistic. Their empathy and creativity allows them to connect deeply with others and express themselves uniquely.")
                print("Weaknesses:  Conversely, Pisces can be overly idealistic and escapist. Their sensetivity may lead to vulnerability and avoidance of reality.")
                print("Your symbol is:  Fish")
                print("Your lucky number is:  11")
                print("Your planet / star is:  Neptune")
                print(" ")
                time.sleep(3)
                Western = False
        elif month == 'april':
            astro_sign = 'Aries' if (day < 20) else 'Taurus'
            if astro_sign == 'Aries':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Aries are known for their courage and determination. Their leadership skills are unmatched, and they tackle challenges head-on with an infectious enthusiasm.")
                print("Weaknesses:  However, they can be impulsive and quick-tempered. Their competitive nature sometimes leads to impatience and conflicts.")
                print("Your symbol is:  Ram")
                print("Your lucky number is:  5")
                print("Your planet / star is:  Mars")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Taurus':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Taurus individuals are reliable and patient. Their strong sense of loyalty and love for beauty and comfort make them dependable friends and partners.")
                print("Weaknesses:  They can be stubborn and resistant to change. Their desire for comfort may lead to materialism and overindulgence.")
                print("Your symbol is:  Bull")
                print("Your lucky number is:  6")
                print("Your planet / star is:  Venus")
                print(" ")
                time.sleep(3)
                Western = False
        elif month == 'may':
            astro_sign = 'Taurus' if (day < 21) else 'Gemini'
            if astro_sign == 'Gemini':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Gemini's are adaptable and quick-witted. Their curiosity and communication skills allow them to connect with people effortlessly and learn new things rapidly.")
                print("Weaknesses:  Conversely, Gemini's can be indecisive and inconsistent. Their dual nature sometimes makes them appear superficial or unreliable.")
                print("Your symbol is:  Twins")
                print("Your lucky number is:  7")
                print("Your planet / star is:  Mercury")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Taurus':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Taurus individuals are reliable and patient. Their strong sense of loyalty and love for beauty and comfort make them dependable friends and partners.")
                print("Weaknesses:  They can be stubborn and resistant to change. Their desire for comfort may lead to materialism and overindulgence.")
                print("Your symbol is:  Bull")
                print("Your lucky number is:  6")
                print("Your planet / star is:  Venus")
                print(" ")
                time.sleep(3)
                Western = False
        elif month == 'june':
            astro_sign = 'Gemini' if (day < 21) else 'Cancer'
            if astro_sign == 'Gemini':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Gemini's are adaptable and quick-witted. Their curiosity and communication skills allow them to connect with people effortlessly and learn new things rapidly.")
                print("Weaknesses:  Conversely, Gemini's can be indecisive and inconsistent. Their dual nature sometimes makes them appear superficial or unreliable.")
                print("Your symbol is:  Twins")
                print("Your lucky number is:  7")
                print("Your planet / star is:  Mercury")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Cancer':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Cancer signs are incredibly intuitive and empathetic. Their nurturing nature makes them excellent caregivers, deeply attuned to the needs of others.")
                print("Weaknesses:  Yet, Cancers can be overly sentitive and moody. Their strong attachment to the past can lead to clinginess and difficulty letting go.")
                print("Your symbol is:  Crab")
                print("Your lucky number is:  2")
                print("Your planet / star is:  Moon")
                print(" ")
                time.sleep(3)
                Western = False
        elif month == 'july':
            astro_sign = 'Cancer' if (day < 23) else 'Leo'
            if astro_sign == 'Leo':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Leos exude confidence and charisma. Their natural leadership and generosity make them the life of the party and a source of inspiration.")
                print("Weaknesses:  However, Leo's can be arrogant and domineering. Their desire for admiration may lead to vanity and stubbornness.")
                print("Your symbol is:  Lion")
                print("Your lucky number is:  19")
                print("Your planet / star is:  The Sun")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Cancer':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Cancer signs are incredibly intuitive and empathetic. Their nurturing nature makes them excellent caregivers, deeply attuned to the needs of others.")
                print("Weaknesses:  Yet, Cancers can be overly sentitive and moody. Their strong attachment to the past can lead to clinginess and difficulty letting go.")
                print("Your symbol is:  Crab")
                print("Your lucky number is:  2")
                print("Your planet / star is:  Moon")
                print(" ")
                time.sleep(3)
                Western = False
        elif month == 'august':
            astro_sign = 'Leo' if (day < 23) else 'Virgo'
            if astro_sign == 'Leo':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Leos exude confidence and charisma. Their natural leadership and generosity make them the life of the party and a source of inspiration.")
                print("Weaknesses:  However, Leo's can be arrogant and domineering. Their desire for admiration may lead to vanity and stubbornness.")
                print("Your symbol is:  Lion")
                print("Your lucky number is:  19")
                print("Your planet / star is:  The Sun")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Virgo':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Virgo's are known for their meticulous attention to detail and analytical minds. Their practicality and reliability make them excellent problem solvers.")
                print("Weaknesses:  On the flip side, Virgo's can be overly critical and perfectionist. Their high standards may cause anxiety and self-doubt.")
                print("Your symbol is:  Virgin Maiden")
                print("Your lucky number is:  7")
                print("Your planet / star is:  Mercury")
                print(" ")
                time.sleep(3)
                Western = False
        elif month == 'september':
            astro_sign = 'Virgo' if (day < 23) else 'Libra'
            if astro_sign == 'Libra':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Libra's are diplomatic and fair-minded. Their charm and ability to see multiple perspectives help them resolve conflicts and build harminous relationships.")
                print("Weaknesses:  Yet, Libra's can be indecisive and avoid confrontations. Their desire for peace may lead to people-pleasing and lack of assertiveness.")
                print("Your symbol is:  Scales")
                print("Your lucky number is:  3")
                print("Your planet / star is:  Venus")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Virgo':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Virgo's are known for their meticulous attention to detail and analytical minds. Their practicality and reliability make them excellent problem solvers.")
                print("Weaknesses:  On the flip side, Virgo's can be overly critical and perfectionist. Their high standards may cause anxiety and self-doubt.")
                print("Your symbol is:  Virgin Maiden")
                print("Your lucky number is:  7")
                print("Your planet / star is:  Mercury")
                print(" ")
                time.sleep(3)
                Western = False
        elif month == 'october':
            astro_sign = 'Libra' if (day < 23) else 'Scorpio'
            if astro_sign == 'Libra':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Libra's are diplomatic and fair-minded. Their charm and ability to see multiple perspectives help them resolve conflicts and build harminous relationships.")
                print("Weaknesses:  Yet, Libra's can be indecisive and avoid confrontations. Their desire for peace may lead to people-pleasing and lack of assertiveness.")
                print("Your symbol is:  Scales")
                print("Your lucky number is:  3")
                print("Your planet / star is:  Venus")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Scorpio':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Scorpio's are passionate and resourceful. Their determination and emotional depth make them a powerful allies and formidable opponents.")
                print("Weaknesses:  Conversely, Scorpio's can be secretive and possessive. Their intensity may lead to jealousy and a tendency to hold grudges.")
                print("Your symbol is:  Scorpion")
                print("Your lucky number is:  4")
                print("Your planet / star is:  Pluto")
                print(" ")
                time.sleep(3)
                Western = False
        elif month == 'november':
            astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
            if astro_sign == 'Sagittarius':
                print(" ")
                Western = False
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Sagittarians are adventurous and optimistic. Their love for freedom and exploration drives them to seek new experiences and knowledge.")
                print("Weaknesses:  However, Sagittarians can be blunt and impatient. Their quest for adventure may lead to restlessness and lack of commitment")
                print("Your symbol is:  Archer")
                print("Your lucky number is:  6")
                print("Your planet / star is:  Jupiter")
                print(" ")
                time.sleep(3)
                Western = False
            if astro_sign == 'Scorpio':
                print(" ")
                print("Your Astrological sign is :", astro_sign)
                print("Strengths:  Scorpio's are passionate and resourceful. Their determination and emotional depth make them a powerful allies and formidable opponents.")
                print("Weaknesses:  Conversely, Scorpio's can be secretive and possessive. Their intensity may lead to jealousy and a tendency to hold grudges.")
                print("Your symbol is:  Scorpion")
                print("Your lucky number is:  4")
                print("Your planet / star is:  Pluto")
                print(" ")
                time.sleep(3)
                Western = False
        else:
            print("Unknown month submitted")

def chinese():
    Chinese = True
    while Chinese == True:
        year = int(input("Input your birth year: "))

        if (year - 2000) % 12 == 0:
            sign = 'Dragon'
            if sign == 'Dragon':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Confident, intelligent, enthusiastic")
                print("Lucky Colours:  Gold, Silver, Grayish White")
                print("Lucky Numbers:  1, 6, 7")
                print("Lucky Flowers:  Bleeding Heart Vine, Dragon Flowers")
                print(" ")
                time.sleep(3)
                Chinese = False
        elif (year - 2000) % 12 == 1:
            sign = 'Snake'
            if sign == 'Snake':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Enigmatic, intelligent, wise")
                print("Lucky Colours:  Black, Red, Yellow")
                print("Lucky Numbers:  2, 8, 9")
                print("Lucky Flowers:  Orchid, Cactus")
                print(" ")
                time.sleep(3)
                Chinese = False
        elif (year - 2000) % 12 == 2:
            sign = 'Horse'
            if sign == 'Horse':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Animated, active, Energetic")
                print("Lucky Colours:  Yellow, Green")
                print("Lucky Numbers:  2, 3, 7")
                print("Lucky Flowers:  Calla Lily, Jasmine")
                print(" ")
                time.sleep(3)
                Chinese = False
        elif (year - 2000) % 12 == 3:
            sign = 'Goat'
            if sign == 'Goat':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Calm, Gentle, sympathetic")
                print("Lucky Colours:  Brown, Red, Purple")
                print("Lucky Numbers:  2, 7")
                print("Lucky Flowers:  Carnations, Primroses")
                print(" ")
                time.sleep(3)
                Chinese = False
        elif (year - 2000) % 12 == 4:
            sign = 'Monkey'
            if sign == 'Monkey':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Sharp, Smart, Curious")
                print("Lucky Colours:  White, Blue, Gold")
                print("Lucky Numbers:  4, 9")
                print("Lucky Flowers:  Chrysanthemum, Crape myrtle")
                print(" ")
                time.sleep(3)
                Chinese = False
        elif (year - 2000) % 12 == 5:
            sign = 'Rooster'
            if sign == 'Rooster':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Observant, Hardworking, Courageous")
                print("Lucky Colours:  Gold, Brown, Yellow")
                print("Lucky Numbers:  5, 7, 8")
                print("Lucky Flowers:  Gladiola, Cockscomb")
                print(" ")
                time.sleep(3)
                Chinese = False
        elif (year - 2000) % 12 == 6:
            sign = 'Dog'
            if sign == 'Dog':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Lovely, Honest, Prudent")
                print("Lucky Colours:  Red, Green, Purple")
                print("Lucky Numbers:  3, 4, 9")
                print("Lucky Flowers:  Rose, Cymbidium Orchids")
                print(" ")
                time.sleep(3)
                Chinese = False
        elif (year - 2000) % 12 == 7:
            sign = 'Pig'
            if sign == 'Pig':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Compassionate, Generous, Diligent")
                print("Lucky Colours:  Yellow, Gray, Brown, Gold")
                print("Lucky Numbers:  2, 5, 8")
                print("Lucky Flowers:  Hydrangea, Daisy")
                print(" ")
                time.sleep(3)
                Chinese = False
        elif (year - 2000) % 12 == 8:
            sign = 'Rat'
            if sign == 'Rat':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Quick-witted, Resourceful, Versatile, Kind")
                print("Lucky Colours:  Blue, Gold, Green")
                print("Lucky Numbers:  2, 3")
                print("Lucky Flowers:  Lily, African Violet")
                print(" ")
                time.sleep(3)
                Chinese = False
        elif (year - 2000) % 12 == 9:
            sign = 'Ox'
            if sign == 'Ox':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Diligent, Dependable, Strong, Determined")
                print("Lucky Colours:  White, Yellow, Green")
                print("Lucky Numbers:  1, 4")
                print("Lucky Flowers:  Tulip, Peach Blossom")
                print(" ")
                time.sleep(3)
                Chinese = False
        elif (year - 2000) % 12 == 10:
            sign = 'Tiger'
            if sign == 'Tiger':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Brave, Confident, Competitive")
                print("Lucky Colours:  Blue, Gray, Orange")
                print("Lucky Numbers:  1, 3, 4")
                print("Lucky Flowers:  Yellow Lily, Cineraria")
                print(" ")
                time.sleep(3)
                Chinese = False
        else:
            sign = 'Rabbit'
            if sign == 'Rabbit':
                print(" ")
                print("Your Zodiac sign :", sign)
                print("Personality Traits:  Quiet, Elegant, King, Responsible")
                print("Lucky Colours:  Red, Pink, Blue, Purple")
                print("Lucky Numbers:  3, 4, 6")
                print("Lucky Flowers:  Plantain Lily, Jasmine")
                print(" ")
                time.sleep(3)
                Chinese = False

while Running == True:
    userInput = input("Input choice (western / chinese): ")
    if userInput == "western":
        western()    
    elif userInput == "Western":
        western()
    elif userInput == "chinese":
        chinese()
    elif userInput == "Chinese":
        chinese()
    elif userInput == "Quit":
        Running = False
        if Running == False:
            print("Exiting")
            time.sleep(3)
            quit()
    elif userInput == "quit":
        Running = False
        if Running == False:
            print("Exiting")
            time.sleep(3)
            quit()
    else:
        print(" ")
        print("Unknown input")