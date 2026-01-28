# IBiB Sumobot Arena Rules

**Event Summary:** Two robots compete in a head-to-head match following the basic system of traditional human sumo wrestling. Robots are autonomous. The objective is for a robot to push its opponent outside of the arena (doyho).

## I. Event Structure

### A. Arena

1. Competition area
    1. The name of the competition area is *dohyo*.
    2. The ring shall be circular in shape and 76 cm-77 cm (30 inches) in diameter. 
    3. The surface will be painted black or be blackbplastic with a 1 cm white line for a border. 
    4. The ring area extends to the outside edge of this circular line. 
    5. The dohyo will be at least 2.5cm in thickness.
2. Shikiri lines (starting lines) 
    1. Two painted parallel brown (or equivalent for absorption of IR light) lines centered in the ring
    2. The dimension of the shikiri lines are 1 cm in width, 10cm in length.
    3. The shikiri lines are spaced 10cm apart. 
    4. The separation distance between the lines is measured to their outside edges.
3. Dohyo exterior
    1. The area surrounding the dohyo is the *Shuhen*.
    2. There should be an appropriate space for recovering robots outside the outer edge of the ring. 
        1. This space can be of any color, and can be of any material or shape as long as the basic concepts of these rules are not violated. 
    2. This area, with the ring in the middle, is to be called the *arena*. 

**comments** The exact material for the dohyo is not specified. It may not be necessary to specify a material, only a set of characteristics such that the edge detection sensors can be adjusted to trigger only on the border and not on the shikiri lines and that the surface is suitable for the standard 2040b class blade and wheels. Should we add a diagram of the dohyo? Should we have a minimum distance for the shuhen?

### B. Format

1. The event is a double-elimination tournament. 
    1. Seeding is done randomly based upon the number of contestants entering the competition. 
    2. In the event that the bracket incorporates byes, they will be filled randomly.
2. Each robot competes in matches consisting of up to three bouts.
3. The winner of a match is the robot that wins two out of three bouts.
4. The winner of each match moves on in the winners bracket.
5. The loser of each match, if it is their first loss, moves to the losers bracket.
6. Ties are addressed in the section `C. Bout`
7. A robot is eliminated from the event after its second loss.
8. The judge overseeing the event is the gyoji.

### C. Bout 

1. A bout lasts a maximum of three minutes.
2. Contestant Positioning
    1. Contestants stand by the dohyo behind their respective shikiri lines.
3. Robot placement
    1. At the gyoji's command of "Position bots," contestants must immediately hold their robots directly over the area they intend to place them, approximately 15cm (6 inches) above the dohyo.
    2. The gyoji will then give the command "Place Bots," at which point contestants must lower their robots straight down onto the dohyo in one continuous motion, ensuring the final orientation is set during this movement.
    3. No additional adjustments to the robot's position or orientation are allowed after it has been placed on the dohyo.
    4. Failing to comply with these placement rules may be considered a minor violation. 
4. Starting the bout
    1. The robots must conform to the startup sequence described in `II.A. startup sequence`
    1. The gyoji instructs the contestants to arm their robots.
    2. With a countdown ("three, two, one, release"), the contestants initiate the start sequence of their robots and step away from the dohyo.
        1. Contestants should step away at least 30 inches from the edge of the dohyo.
5. False Start
    1. The gyoji may declare a false start if a robot starts before the word "release".
    2. The gyoji will declare a false start if they hear an audible sound from one of the robots prior to saying the word "release".
    3. After a false start, the offending robot is issued a penalty (shido).
    4. A robot receiving two shidos loses the bout.
6. Scoring and stopping the bout
    1. Earning points (Yuhkoh):
        1. A Yuhkoh is earned when a robot successfully pushes its competitor outside of the dohyo.
        2. A Yuhkoh is also earned if the competitor's robot exits the dohyo on its own.
        3. A Yuhkoh is awarded to a robot if its competitor receives two shidos.
    2. The Gyoji may stop a bout under several conditions
        1. A player is injured or about to be injured.
        2. The robots display no forward progress in the bout for 10 seconds.
        3. A robot is about to damage the dohyo.
        4. A robot has violated one of the rules.        
    3. Should a bout end with no contestant leaving the dohyo, gyoji will decide a winner and award a yuhkoh based upon technical merits in movement and operation of the robot, penalties accrued during the bout, and contestant attitudes during the bout.

**Comments** Should we provide examples of the decision making process in the event of a tie? It is possible that the gyoji cannot differentiate between the two sounds the robots are making, and therefore makes it difficult to determine who commits a false start. 

## II. Additional robot regulations

### A. Startup sequence
1. A startup sequence must be initiated by the press of button GP20
    1. Pressing and holding the GP20 button is referred to as "arming the robot".
    2. Releasing the GP20 button will continue the startup sequence.
2. The startup sequence must emit an audible tone to indicate the sequence has started
3. The startup sequence must blink the neopixel LEDs at 1 second intervals
4. The startup sequence must last for at least 5 seconds.
5. The wheel motors must be off during the startup sequence.

### B. Robot upgrades during competition
1. Contestants are not allowed to modify their robots after completing the class verification procedure unless specificly mentioned in these rules.
2. Sensor calibration (e.g. adjusting the potentiometers of edge detectors) 
    1. Utilizing the dohyo for sensor calibration is allowed prior to the start of the competition. 
    2. Contestants my not calibrate any sensors during their match.
    3. Contestants may perform sensor calibration without the use of the dohyo at other times during the competition.
3. Power (e.g. checking and replacing batteries)
    1. Batteries cannot be replaced after robots have completed their calss verification procedure.
    2. Under special circumstances, gyoji or the event manager may permit battery replacements, which will require class reverification. 

**Comments** Should we indicate the frequency and duration of the startup tone? Are there other startup sequence standardizations that should be implemented? Note that the mass difference between the super cheap zinc oxide and standard alkaline batteries is significant, so battery swap outs could result in a verified bot exceeding the weight limit.

## III. Violations and penalties

### A. Violations

1. Major violations
    1. A player who utters insulting words or puts voice devices in a robot to utter insulting words, or writes insulting words on teh body of a robot, is in violation of these rules.
2. Minor violations
    1. Entering the arena during the round without legitimate reason.
    2. Demanding to stop a match without appropriate reason.
    3. Taking more than 30 seconds before resuming a bout unless gyoji has announced a time extension.

### B. Penalties

1. In the event of a major violation, the contestant receives a kinjite (disqualification). All robots entered under the contestant are removed from the event.
2. In the event of minor violoation, the offending robot recieves a shido. Two shidos within one bout results in a Yuhkoh for the opponent.

## IV. Miscellaneous

### A. Declaring objections
1. No objections shall be declared against gyoji's decisions

### B. Safety Protocols
1. *reserved*

### C. Code of Conduct
1. *reserved*

### D. Technical Support
1. *reserved*

## V. Definitions

Bout
: A single 3-minute competition between two robots

Event
: A series of matches organized into a double-elimination bracket

Gyoji
: The referee/judge of a match.

Kinjite
: Disqualification from an event due to a major violation of the rules.

Match
: A series of up to three bouts

Shido
: A minor penalty. Two shidos within a bout results in a Yuhkoh for the opponent.

Yuhkoh
: A point, indicating that a bout has been won.