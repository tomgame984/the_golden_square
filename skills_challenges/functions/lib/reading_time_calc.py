import string

def reading_time_calculator(text):
    wpm = 200
    word_count = sum([i.strip(string.punctuation).isalpha() for i in text.split()])
    reading_time = (word_count/wpm)
    if word_count == 0:
        return 'There are no words to read!'
    
    else:
        if reading_time > 1:
            return f"This text will take about {round(reading_time)} minute(s) to read."
    
        else:
            return "This text will take less than a minute to read."
        

    


# TEXT STRINGS
one_hundred_words = """The Le Mans 24 Hours is a renowned endurance race held in Le Mans, France. Originating in 1923, it features a challenging 13.626-kilometer circuit with iconic sections like the Mulsanne Straight. Teams compete across multiple classes, including prototypes and production-based sports cars, striving to cover the greatest distance within 24 hours. The race demands strategic pit stops, driver changes, and endurance amidst changing weather and traffic conditions. With a rich history of legendary drivers, iconic moments, and technological innovation, the Le Mans 24 Hours remains a pinnacle event in motorsport, captivating global audiences with its blend of speed, skill, and endurance."""

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