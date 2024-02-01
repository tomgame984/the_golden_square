# {{Reading Time Calculator}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

```python
def reading_time_calculator(text_string, wpm = 200):
"""Calculates the number of minutes it will take to read a trxt string based on a reading speed of 200 words per minute (WPM).

Parameters:
    text_string: a string of the the text the user is intending to read.
    wpm: reading speed of the user, default value is 200.

Returns:
    a print statement: 'Based on {WPM} words per minute, this text will take {x} minutes to read.'
"""
    pass

two_hundred_words = """The Le Mans 24-hour race is a legendary endurance event held annually in Le Mans, France. It is one of the most prestigious and grueling races in motorsport. Teams from around the world compete in various classes, including prototypes and production-based sports cars, striving to cover the greatest distance within 24 hours. The event tests not only the speed of the cars but also the endurance of the drivers and the reliability of the machinery.

The race begins with a spectacular rolling start, with cars jostling for position as they charge down the famous Mulsanne Straight. Throughout the day and night, drivers navigate a challenging circuit that combines high-speed straights with tight chicanes and sweeping curves, all while contending with changing weather conditions and traffic from other classes.

Teams employ strategic pit stops for refueling, tire changes, and driver swaps, aiming to minimize time lost while maximizing performance. The race often sees intense battles for position and dramatic moments as cars push the limits of speed and endurance.

Ultimately, the team that completes the most laps or covers the farthest distance within the 24-hour timeframe emerges victorious, earning not only a place in motorsport history but also the respect of fans and competitors alike. The Le Mans 24-hour race stands as a true test of skill, teamwork, and determination in the world of endurance racing."""

two_thousand_words = """The Le Mans 24 Hours, often simply referred to as Le Mans, is an iconic endurance race held annually in Le Mans, France. It stands as one of the most revered and challenging events in motorsport, attracting teams, drivers, and fans from around the world. This comprehensive summary will delve into the rich history, the unique challenges, the evolution of the race, notable moments, and its enduring legacy.

### History and Origins

The origins of the Le Mans 24 Hours trace back to the early 20th century. The Automobile Club de l'Ouest (ACO) conceived the idea as a means to showcase automobile endurance and innovation. The inaugural race took place in 1923 on public roads near the town of Le Mans. The event's format, comprising a full day of racing, was groundbreaking and captured the imagination of motorsport enthusiasts.

### Evolution of the Race

Over the decades, the Le Mans 24 Hours has evolved significantly. The circuit itself has undergone numerous modifications to enhance safety and accommodate technological advancements in racing cars. The race has seen periods of dominance by various manufacturers, each bringing their own engineering prowess and competitive spirit to the event.

### The Circuit

The Circuit de la Sarthe, as it is officially known, is a challenging 13.626-kilometer (8.469-mile) track. It combines fast straights, tight chicanes, and sweeping curves, including iconic sections like the Mulsanne Straight and the Porsche Curves. The circuit's mix of high-speed sections and technical corners presents a unique test of both driver skill and machine endurance.

### Racing Classes

The Le Mans 24 Hours features multiple racing classes, each catering to different types of cars and levels of performance. The top category, known as Le Mans Prototype (LMP), consists of two classes: LMP1 and LMP2. These prototypes feature cutting-edge technology and aerodynamics, pushing the boundaries of automotive engineering. Additionally, the race includes several categories for production-based sports cars, such as the GT classes, which showcase vehicles from renowned manufacturers like Ferrari, Porsche, and Aston Martin.

### Race Format

The race follows a unique format: teams compete to cover the greatest distance within a 24-hour period. The event kicks off with a dramatic rolling start, with cars jostling for position as they charge down the long Mulsanne Straight. Throughout the day and night, drivers face the dual challenges of fatigue and concentration, navigating the circuit while contending with traffic from other classes and changing weather conditions.

Strategic pit stops play a crucial role in the race, allowing teams to refuel, change tires, and perform repairs. Driver changes also occur during pit stops, ensuring that each team's roster remains fresh and capable of tackling the demanding conditions.

### The Importance of Strategy

Strategy is paramount in the Le Mans 24 Hours. Teams must balance speed with reliability, knowing when to push their cars to the limit and when to conserve resources for the long haul. The ability to adapt to changing circumstances, such as weather fluctuations or mechanical issues, can often determine the outcome of the race.

### Endurance and Reliability

Endurance and reliability are hallmarks of the Le Mans 24 Hours. Unlike traditional sprint races, which focus on raw speed, endurance racing demands durability and resilience from both drivers and machines. Cars must withstand the rigors of continuous operation for an entire day, enduring high speeds, intense heat, and mechanical stress without faltering.

### Iconic Moments and Legendary Drivers

The history of the Le Mans 24 Hours is punctuated by iconic moments and legendary drivers. From epic duels on the track to heart-stopping finishes, the race has produced countless moments of drama and excitement. Drivers like Tom Kristensen, Jacky Ickx, and Derek Bell have achieved multiple victories at Le Mans, cementing their status as enduring figures in motorsport history.

### Technological Innovation

The Le Mans 24 Hours has long been a hotbed of technological innovation. Manufacturers use the race as a proving ground for new technologies, pushing the boundaries of performance, efficiency, and safety. Innovations such as hybrid powertrains, aerodynamic advancements, and lightweight materials have all found their way from the race track to the showroom, shaping the future of automotive engineering.

### Environmental Sustainability

In recent years, the Le Mans 24 Hours has placed increasing emphasis on environmental sustainability. Organizers and manufacturers alike are exploring ways to reduce the ecological footprint of the race, implementing measures such as hybrid and electric propulsion systems and promoting eco-friendly practices throughout the event.

### Global Impact

The Le Mans 24 Hours enjoys a global audience, with millions of fans tuning in to watch the race live or following the action online. The event's rich history and unique challenges have earned it a special place in the hearts of motorsport enthusiasts worldwide. It serves as a showcase of human ingenuity, teamwork, and passion for automotive excellence.

### Conclusion

The Le Mans 24 Hours stands as a testament to the enduring spirit of endurance racing. From its humble beginnings in the 1920s to its status as one of the premier events in motorsport today, the race continues to captivate audiences with its blend of speed, skill, and strategy. As technology evolves and new challenges emerge, the Le Mans 24 Hours remains a symbol of innovation and excellence in the world of motorsport."""

one_hundred_words = """The Le Mans 24 Hours is a renowned endurance race held in Le Mans, France. Originating in 1923, it features a challenging 13.626-kilometer circuit with iconic sections like the Mulsanne Straight. Teams compete across multiple classes, including prototypes and production-based sports cars, striving to cover the greatest distance within 24 hours. The race demands strategic pit stops, driver changes, and endurance amidst changing weather and traffic conditions. With a rich history of legendary drivers, iconic moments, and technological innovation, the Le Mans 24 Hours remains a pinnacle event in motorsport, captivating global audiences with its blend of speed, skill, and endurance."""
```

## 3. Create Examples as Tests

```python
"""
Given a string with 200 words and no change to the WPM
Returns a statement of 'Based on 200 words per minute, this text will take 1 minutes to read.'
"""
reading_time_calculator(two_hundred_words) => 'Based on 200 words per minute, this text will take about 1 minute to read.'

"""
Given a string with 200 words and the WPM changed to 100.
Returns a statement of 'Based on 100 words per minute, this text will take 2 minutes to read.'
"""
reading_time_calculator(two_hundred_words) => 'Based on 100 words per minute, this text will take about 2 minutes to read.'

"""
Given a string with 100 words and no change to the WPM
Returns a statement of 'Based on 200 words per minute, this text will less than a minute to read.'
"""
reading_time_calculator(one_hundred_words) => 'Based on 200 words per minute, his text will less than a minute to read.'

"""
Given a string with 2000 words and no change to the WPM.
Returns a statement of 'Based on 200 words per minute, this text will take 10 minutes to read.'
"""
reading_time_calculator(two_thousand_words) => 'Based on 200 words per minute, his text will take about 10 minutes to read.'

"""
Given a empty string with n words and no change to the WPM.
Returns a statement of 'There is nothing to read!'
"""
reading_time_calculator("") => 'There is nothing to read!'
```

## 4. Implement the Behaviour

See test_reading_time_calc.py
