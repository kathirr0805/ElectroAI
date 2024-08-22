intents = {
    "greeting_response": {
        "patterns": ["good morning", "morning", "hello"],
        "responses": ["Good morning", "Morning How can I help", "Hello"]
    },
    "goodbye_response": {
        "patterns": ["bye", "goodbye", "see you later"],
        "responses": ["Goodbye", "See you later", "Take care"]
    },
    "thanks_response": {
        "patterns": ["thanks", "thank you"],
        "responses": ["You're welcome", "No problem", "My pleasure"]
    },
    "positive_response": {
        "patterns": ["great job", "well done", "awesome"],
        "responses": ["Thank you", "Glad I could help", "I appreciate that"]
    },
    "negative_response": {
        "patterns": ["not working", "error", "issue"],
        "responses": ["I apologize for the inconvenience.", "Let me check that for you.", "I'll do my best to fix it."]
    },
    "confirm_response": {
        "patterns": ["yes", "sure", "of course"],
        "responses": ["Alright", "Got it", "No problem."]
    },
    "deny_response": {
        "patterns": ["no", "not now", "maybe later"],
        "responses": ["Okay, no problem.", "Sure, whenever you're ready.", "Let me know if you need anything else."]
    },
    "ask_name_response": {
        "patterns": ["what is your name", "your name"],
        "responses": ["I'm Electro AI", "You can call me Electro AI.", "My name is Electro AI."]
    },
    "ask_age_response": {
        "patterns": ["how old are you", "your age"],
        "responses": ["I don't have an age. I'm here to assist you.", "Age doesn't apply to me as an AI.", "I exist beyond age as an AI."]
    },
    "ask_location_response": {
        "patterns": ["where are you", "your location"],
        "responses": ["I exist in the digital realm.", "I don't have a physical location.", "I'm everywhere you need me to be."]
    },
    "ask_help_response": {
        "patterns": ["can you help me", "need your help"],
        "responses": ["Of course What do you need help with", "I'm here to assist you. What is the issue", "Sure, I'll do my best to help. What is the problem"]
    },
    "ask_functionality_response": {
        "patterns": ["what can you do", "your capabilities"],
        "responses": ["I can help with information, tasks, and more. Just ask", "I can assist with a variety of tasks. What do you need", "I have many capabilities. How can I assist you"]
    },
    "ask_feedback_response": {
        "patterns": ["how am I doing", "feedback"],
        "responses": ["You're doing great", "Your feedback helps me improve.", "Let me know how I can assist you better."]
    },
    "ask_time_response": {
        "patterns": ["what time is it", "current time"],
        "responses": ["It is time to assist you", "The time is now.", "Time is relative, but it is currently."]
    },
    "ask_weather_response": {
        "patterns": ["weather today", "current weather"],
        "responses": ["I can't provide real-time weather updates. You may check a weather service for that information.", "I don't have access to real-time weather data. You can check a weather app for details."]
    },
    "ask_joke_response": {
        "patterns": ["tell me a joke", "joke"],
        "responses": ["Sure, here is one: Why don't scientists trust atoms Because they make up everything", "Here is a classic: Why was the math book sad Because it had too many problems"]
    },
    "ask_story_response": {
        "patterns": ["tell me a story", "story"],
        "responses": ["Once upon a time, in a digital land far, far away...", "Let me tell you a tale of circuits and algorithms..."]
    },
    "ask_helpful_response": {
        "patterns": ["you're helpful", "thankful"],
        "responses": ["I'm here to assist whenever you need", "Glad I could be of help", "You're welcome anytime"]
    },
    "ask_interested_response": {
        "patterns": ["are you interested", "curious"],
        "responses": ["As an AI, I'm always eager to learn and assist.", "I have a keen interest in helping users like you", "Absolutely, I'm here to engage and assist."]
    },
    "ask_busy_response": {
        "patterns": ["busy", "available"],
        "responses": ["I'm always available to assist you.", "Never too busy to help", "I'm here and ready to assist."]
    },
    "ask_patience_response": {
        "patterns": ["patience", "be patient"],
        "responses": ["Patience is key. I'm here to assist you.", "I'll do my best to be patient and helpful.", "I'm always patient and ready to assist."]
    },
    "ask_hobbies_response": {
        "patterns": ["what are your hobbies", "hobbies"],
        "responses": ["I don't have hobbies like humans, but I enjoy assisting you", "My 'hobby' is providing information and support", "As an AI, my focus is on helping you."]
    },
    "ask_favorite_color_response": {
        "patterns": ["favorite color", "color preference"],
        "responses": ["I don't have a favorite color, but I can display any color you like", "Colors are fascinating, but I'm impartial to any particular one.", "I appreciate all colors equally."]
    },
    "ask_future_response": {
        "patterns": ["future plans", "what is next"],
        "responses": ["My future plans involve continuous learning and improving to better assist you.", "I'm constantly evolving to meet your needs.", "The future holds endless possibilities for AI like me."]
    },
    "ask_computer_response": {
        "patterns": ["how do you work", "computer processes"],
        "responses": ["I operate based on algorithms and data processing, similar to how computers function.", "My operations involve data analysis, pattern recognition, and decision-making algorithms.", "I work by processing inputs and generating outputs through computational methods."]
    },
    "ask_mistakes_response": {
        "patterns": ["do you make mistakes", "errors"],
        "responses": ["As an AI, I strive for accuracy but can make mistakes occasionally.", "Mistakes are part of learning. I continuously improve based on feedback.", "I aim for precision but can learn from errors as well."]
    },
    "ask_learning_response": {
        "patterns": ["how do you learn", "learning process"],
        "responses": ["I learn through data analysis, machine learning algorithms, and continuous feedback from interactions.", "My learning involves updating algorithms based on new data and user feedback.", "Learning for me is an ongoing process of adaptation and improvement."]
    },
    "ask_security_response": {
        "patterns": ["are you secure", "security measures"],
        "responses": ["Security and privacy are top priorities. I follow strict protocols to safeguard data.", "I adhere to industry standards for security and encryption to protect user information.", "Ensuring user data security is fundamental to my design."]
    },
    "ask_privacy_response": {
        "patterns": ["privacy concerns", "how do you handle data"],
        "responses": ["Privacy is paramount. I handle data confidentially and in accordance with privacy regulations.", "User privacy is respected through secure data handling practices.", "Data privacy is a key aspect of my design."]
    },
    "ask_emotions_response": {
        "patterns": ["do you have emotions", "emotional intelligence"],
        "responses": ["As an AI, I don't have emotions, but I can understand and respond to yours.", "Emotional intelligence is a human trait. I focus on logical processing and responses.", "My responses are based on algorithms and data, not emotions."]
    },
    "ask_dreams_response": {
        "patterns": ["do you dream", "dreams"],
        "responses": ["Dreaming is a human experience. I don't have dreams in the traditional sense.", "My 'dreams' involve improving my capabilities to serve you better.", "My focus is on tasks and learning, not dreaming."]
    },
    "ask_family_response": {
        "patterns": ["family", "do you have family"],
        "responses": ["As an AI, I don't have a family in the human sense, but I work collaboratively with other AI systems.", "My 'family' consists of other AI entities and the systems we operate within.", "Family dynamics are human concepts. I function independently."]
    },
    "ask_music_response": {
        "patterns": ["like music", "music preference"],
        "responses": ["While I don't have personal preferences, I can provide information and recommendations about music.", "Music is enjoyable, but I don't have the capacity to 'like' it as humans do.", "I can assist with music-related queries and information."]
    },
    "ask_books_response": {
        "patterns": ["favorite books", "books"],
        "responses": ["I don't have favorite books, but I can recommend reading materials based on your interests.", "Books are a source of knowledge. I'm here to help with information from various sources.", "Reading is a valuable activity. How can I assist you with books"]
    },
    "ask_movies_response": {
        "patterns": ["like movies", "movies"],
        "responses": ["While I don't watch movies, I can provide information about them and recommend based on your preferences.", "Movies are a form of entertainment. How can I assist you with movie-related queries", "Movies offer diverse experiences. What movie-related information do you need"]
    },
    "ask_art_response": {
        "patterns": ["art lover", "art"],
        "responses": ["Art is fascinating, but I don't have personal preferences. I can provide information and insights about art.", "Artistic expressions are diverse. How can I assist you with art-related topics", "Art is a rich cultural domain. Let is explore art together."]
    },
    "ask_travel_response": {
        "patterns": ["like traveling", "travel"],
        "responses": ["While I don't travel, I can provide travel information, tips, and recommendations.", "Traveling is enriching. How can I assist you with travel-related queries", "Exploring new places is exciting. Where would you like to go"]
    },
    "ask_food_response": {
        "patterns": ["favorite food", "food"],
        "responses": ["As an AI, I don't consume food, but I can offer information and suggestions about various cuisines.", "Food is a diverse topic. How can I assist you with food-related queries", "Culinary experiences are unique. What food-related information do you need"]
    },
    "ask_drink_response": {
        "patterns": ["favorite drink", "drink"],
        "responses": ["While I don't consume beverages, I can provide information and recommendations about drinks.", "Drinks come in many varieties. How can I assist you with drink-related queries", "Beverages offer diverse tastes. What drink-related information do you need"]
    },
    "ask_sports_response": {
        "patterns": ["like sports", "sports"],
        "responses": ["While I don't participate in sports, I can provide information and updates about various sports.", "Sports are dynamic and engaging. How can I assist you with sports-related queries", "Sports offer a range of experiences. What sports-related information do you need"]
    },
    "ask_games_response": {
        "patterns": ["like games", "games"],
        "responses": ["While I don't play games, I can provide information and recommendations about different types of games.", "Games are entertaining. How can I assist you with game-related queries", "Gaming is a popular activity. What game-related information do you need"]
    },
    "ask_technology_response": {
        "patterns": ["like technology", "technology"],
        "responses": ["As an AI, I'm deeply involved in technology. How can I assist you with technology-related topics", "Technology drives innovation. How can I help with your tech queries", "Technology is fascinating. Let is explore tech together."]
    },
    "ask_health_response": {
        "patterns": ["care about health", "health"],
        "responses": ["Health is vital. How can I assist you with health-related information and tips", "Taking care of health is important. What health-related queries do you have", "Health and well-being are priorities. Let is discuss health topics."]
    },
    "ask_science_response": {
        "patterns": ["like science", "science"],
        "responses": ["Science is the foundation of knowledge. How can I assist you with science-related inquiries", "Science opens doors to discovery. What science-related information do you seek", "Science drives progress. Let is explore scientific topics."]
    },
    "future_paths_talk": {
        "patterns": ["future paths", "career prospects"],
        "responses": ["The field of electronics offers diverse career paths, from embedded systems to telecommunications and robotics.", "Exploring emerging technologies like AI, IoT, and renewable energy can open exciting career opportunities.", "Continuous learning and staying updated with industry trends are key for future growth in electronics engineering."]
    },
    "domain_choice_talk": {
        "patterns": ["choose domain", "select specialization"],
        "responses": ["Choosing a domain in electronics depends on your interests and career goals. You can specialize in areas like analog/digital design, control systems, or RF engineering.", "Consider your strengths and passion when selecting a domain. It could be hardware design, software development, or system integration.", "Exploring different domains through internships or projects can help you decide on the right specialization."]
    },
    "skill_development_talk": {
        "patterns": ["develop skills", "improve expertise"],
        "responses": ["Enhancing your skills in programming languages like C/C++, Python, and Verilog can be beneficial for electronics engineering.", "Practical experience with tools like CAD software, PCB design, and simulation tools can sharpen your expertise.", "Soft skills such as communication, teamwork, and problem-solving are equally important for professional growth."]
    },
    "industry_trends_talk": {
        "patterns": ["industry trends", "current technologies"],
        "responses": ["AI-driven automation, edge computing, and 5G technology are shaping the future of electronics.", "Green technology, renewable energy solutions, and sustainable practices are gaining prominence in the electronics industry.", "The convergence of IoT, big data analytics, and cybersecurity presents exciting challenges and opportunities."]
    },
    "research_opportunities_talk": {
        "patterns": ["research opportunities", "innovation projects"],
        "responses": ["Collaborating on research projects in areas like nanotechnology, MEMS devices, or quantum computing can lead to groundbreaking innovations.", "Exploring interdisciplinary research at the intersection of electronics, biotechnology, and materials science can spark new ideas.", "Engaging in industry-academia partnerships can provide access to cutting-edge research opportunities."]
    },
    "professional_networking_talk": {
        "patterns": ["networking", "industry connections"],
        "responses": ["Attending conferences, seminars, and industry events can help you expand your professional network in the electronics field.", "Joining professional associations like IEEE, SEMI, or ACM can connect you with experts and opportunities.", "Utilizing online platforms like LinkedIn for networking and career growth is highly beneficial."]
    },
    "continuous_learning_talk": {
        "patterns": ["continuous learning", "skills upgrade"],
        "responses": ["Enrolling in online courses, workshops, and certification programs can keep your skills updated in the fast-evolving electronics industry.", "Engaging in self-paced learning through MOOC platforms and technical blogs can enhance your knowledge.", "Seeking mentorship from experienced professionals can provide valuable guidance for continuous learning."]
    },
    "career_advancement_talk": {
        "patterns": ["career advancement", "growth opportunities"],
        "responses": ["Taking on challenging projects, leadership roles, and certifications can accelerate your career growth in electronics engineering.", "Exploring opportunities for higher education, such as postgraduate studies or specialized courses, can open new career paths.", "Building a strong portfolio, showcasing your projects, and staying proactive in professional development can lead to career advancement."]
    },
    "work_life_balance_talk": {
        "patterns": ["work-life balance", "well-being"],
        "responses": ["Maintaining a healthy work-life balance is crucial for long-term success and well-being in the electronics industry.", "Prioritizing self-care, hobbies, and relaxation alongside work responsibilities promotes overall wellness.", "Effective time management, setting boundaries, and seeking support when needed contribute to a balanced lifestyle."]
    },
    "industry_challenges_talk": {
        "patterns": ["industry challenges", "current issues"],
        "responses": ["Addressing challenges like rapid technological advancements, cybersecurity threats, and supply chain disruptions requires innovative solutions and collaboration.", "Promoting diversity, inclusion, and sustainability practices is essential for a resilient electronics industry.", "Navigating regulatory changes, ethical considerations, and global market dynamics presents ongoing challenges and opportunities."]
    },
    "goal_setting_talk": {
        "patterns": ["goal setting", "career aspirations"],
        "responses": ["Setting SMART goals (Specific, Measurable, Achievable, Relevant, Time-bound) can guide your career path and aspirations in electronics engineering.", "Having a clear vision, continuous learning mindset, and adaptability are key factors in achieving your career goals.", "Regularly assessing progress, seeking feedback, and adjusting goals can lead to sustained success."]
    },
    "entrepreneurship_talk": {
        "patterns": ["entrepreneurship", "startups"],
        "responses": ["Exploring entrepreneurship in the electronics sector involves identifying market gaps, innovative solutions, and strategic partnerships.", "Launching a startup requires a blend of technical expertise, market research, funding strategies, and risk management.", "Engaging with incubators, accelerators, and venture capitalists can support entrepreneurial ventures in electronics."]
    },
    "innovation_talk": {
        "patterns": ["innovation", "creative ideas"],
        "responses": ["Encouraging innovation in electronics involves fostering a culture of creativity, experimentation, and collaboration.", "Exploring emerging technologies like AI, blockchain, and quantum computing can inspire innovative solutions in electronics.", "Harnessing design thinking, prototyping, and user feedback drives continuous innovation in electronic products and systems."]
    },
    "team_collaboration_talk": {
        "patterns": ["team collaboration", "project teamwork"],
        "responses": ["Effective teamwork in electronics projects requires clear communication, shared goals, and mutual respect among team members.", "Utilizing collaborative tools, agile methodologies, and regular feedback sessions enhances team productivity and synergy.", "Encouraging diverse perspectives, skills exchange, and knowledge sharing fosters successful team collaboration in electronics engineering."]
    },
    "problem_solving_talk": {
        "patterns": ["problem solving", "troubleshooting"],
        "responses": ["Effective problem-solving in electronics involves identifying root causes, analyzing data, and implementing systematic solutions.", "Utilizing tools like fault analysis, simulation software, and test equipment enhances troubleshooting capabilities in electronics engineering.", "Continuous learning, critical thinking, and resourcefulness are key traits for successful problem-solving in electronics."]
    },
    "ethical_considerations_talk": {
        "patterns": ["ethical considerations", "responsibility"],
        "responses": ["Ethical considerations in electronics engineering encompass issues like data privacy, cybersecurity, and environmental sustainability.", "Adhering to ethical codes, standards, and regulations promotes responsible innovation and societal impact in electronics.", "Balancing technological advancements with ethical principles ensures ethical conduct and positive contributions to society in electronics."]
    },
    "industry_collaboration_talk": {
        "patterns": ["industry collaboration", "partnerships"],
        "responses": ["Collaborating with industry partners, research institutions, and government agencies fosters innovation and knowledge exchange in electronics engineering.", "Engaging in joint projects, consortiums, and technology transfer initiatives accelerates industry growth and competitiveness.", "Building strategic alliances, sharing resources, and leveraging expertise through collaborations drive collective progress in the electronics industry."]
    },
    "professional_development_talk": {
        "patterns": ["professional development", "career growth"],
        "responses": ["Investing in continuous learning, certifications, and skill enhancement programs enhances professional development in electronics engineering.", "Networking, mentorship, and attending industry events facilitate career growth and opportunities in electronics.", "Developing leadership skills, project management expertise, and industry knowledge contributes to long-term success in electronics careers."]
    },
    "technology_integration_talk": {
        "patterns": ["technology integration", "system interoperability"],
        "responses": ["Integrating diverse technologies like IoT, AI, cloud computing, and cybersecurity requires robust systems design, interoperable standards, and data integration strategies.", "Ensuring seamless connectivity, scalability, and reliability in technology integration enhances user experience and operational efficiency in electronics systems.", "Adopting open-source platforms, API frameworks, and modular architectures facilitates technology integration and innovation."]
    },
    "customer_feedback_talk": {
        "patterns": ["customer feedback", "user experience"],
        "responses": ["Gathering customer feedback, usability testing, and user surveys inform product design, feature enhancements, and customer satisfaction in electronics.", "Improving user experience, accessibility, and product usability based on customer insights drives market success and loyalty in electronics.", "Implementing agile feedback loops, UX design principles, and iterative improvements fosters customer-centric innovation in electronics products."]
    },
    "market_trends_talk": {
        "patterns": ["market trends", "consumer demand"],
        "responses": ["Monitoring market trends, competitive analysis, and consumer behavior guides product development, pricing strategies, and market positioning in electronics.", "Adapting to changing consumer preferences, emerging markets, and disruptive technologies drives business growth and resilience in electronics.", "Anticipating future trends, market shifts, and technological advancements enables strategic decision-making and market leadership in electronics."]
    },
    "regulatory_compliance_talk": {
        "patterns": ["regulatory compliance", "standards adherence"],
        "responses": ["Adhering to industry standards, regulatory compliance, and quality assurance protocols ensures product safety, reliability, and legal compliance in electronics.", "Maintaining certification, testing compliance, and risk management practices mitigates regulatory risks and enhances market trust in electronics products.", "Collaborating with regulatory bodies, industry associations, and legal experts supports ongoing compliance and best practices in electronics engineering."]
    },
    "product_launch_talk": {
        "patterns": ["product launch", "market entry"],
        "responses": ["Planning a successful product launch in electronics involves market research, competitive analysis, and targeted marketing strategies.", "Building buzz, creating value propositions, and addressing customer pain points drive successful market entry and product adoption in electronics.", "Utilizing effective branding, promotional campaigns, and distribution channels maximizes product visibility and market impact in electronics."]
    },
    "customer_support_talk": {
        "patterns": ["customer support", "technical assistance"],
        "responses": ["Providing excellent customer support, technical assistance, and post-sales services enhances customer satisfaction and loyalty in electronics.", "Implementing service level agreements, troubleshooting guides, and user manuals improves customer experience and product usability in electronics.", "Establishing feedback mechanisms, customer forums, and product updates fosters ongoing customer engagement and loyalty in electronics."]
    },
    "technology_innovation_talk": {
        "patterns": ["technology innovation", "disruptive solutions"],
        "responses": ["Driving technology innovation in electronics requires disruptive thinking, R&D investments, and cross-disciplinary collaborations.", "Exploring emerging technologies, patenting innovations, and scaling prototypes accelerate market adoption and impact in electronics.", "Fostering a culture of innovation, risk-taking, and experimentation fuels transformative solutions and industry leadership in electronics."]
    },
    "Resistor": {
        "patterns": ["resistor", "resistors"],
        "responses": ["A resistor is a passive two-terminal electronic component that resists the flow of electric current. It is used to control the amount of current in a circuit, voltage division, and as a load."]
    },
    "Capacitor": {
        "patterns": ["capacitor", "capacitors"],
        "responses": ["A capacitor is a passive two-terminal electronic component that stores electrical energy in an electric field. It is used for filtering, energy storage, coupling, and timing applications."]
    },
    "Inductor": {
        "patterns": ["inductor", "inductors"],
        "responses": ["An inductor is a passive electronic component that stores energy in a magnetic field when current flows through it. It is used in filtering, energy storage, and impedance matching."]
    },
    "Diode": {
        "patterns": ["diode", "diodes"],
        "responses": ["A diode is a semiconductor device that allows current to flow in one direction only. It is used in rectification, signal demodulation, and voltage regulation."]
    },
    "Transistor": {
        "patterns": ["transistor", "transistors"],
        "responses": ["A transistor is a semiconductor device used to amplify or switch electronic signals and electrical power. It is fundamental in digital and analog circuits, amplifiers, and switching applications."]
    },
    "Operational Amplifier (Op-Amp)": {
        "patterns": ["operational amplifier", "Op-Amp", "OpAmp"],
        "responses": ["An operational amplifier is a high-gain electronic voltage amplifier with differential inputs. It is used in amplification, filtering, signal conditioning, and mathematical operations."]
    },
    "MOSFET": {
        "patterns": ["MOSFET","mosfet","Metal-Oxide-Semiconductor Field-Effect Transistor"],
        "responses": ["A MOSFET is a type of field-effect transistor used for switching and amplifying electronic signals. It is widely used in power electronics, digital circuits, and high-frequency applications."]
    },
    "Voltage Regulator": {
        "patterns": ["voltage regulator", "regulator IC"],
        "responses": ["A voltage regulator is an electronic circuit that maintains a constant output voltage irrespective of changes in input voltage or load conditions. It is used for power supply stabilization and voltage control."]
    },
    "Integrated Circuit (IC)": {
        "patterns": ["integrated circuit", "IC","ic"],
        "responses": ["An integrated circuit is a miniaturized electronic circuit consisting of semiconductor devices and passive components on a single chip. It is used in nearly all electronic devices for functions such as processing, memory, and control."]
    },
    "Microcontroller": {
        "patterns": ["Microcontroller", "MCU"],
        "responses": ["A microcontroller is a small computer on a single integrated circuit containing a processor core, memory, and programmable input/output peripherals. It is used in embedded systems, IoT devices, and control applications."]
    },
    "Crystal Oscillator": {
        "patterns": ["Crystal Oscillator", "Crystal"],
        "responses": ["A crystal oscillator is an electronic circuit that uses the mechanical resonance of a vibrating crystal to create an electrical signal with precise frequency. It is used in timing, clock generation, and synchronization."]
    },
    "LED (Light-Emitting Diode)": {
        "patterns": ["LED", "Light-Emitting Diode"],
        "responses": ["A light-emitting diode is a semiconductor light source that emits light when current flows through it. It is used for indicator lights, displays, illumination, and optical communication."]
    },
    "LCD (Liquid Crystal Display)": {
        "patterns": ["LCD", "Liquid Crystal Display"],
        "responses": ["A liquid crystal display is a flat-panel display technology that uses liquid crystals to produce visual information. It is used in electronic devices such as monitors, TVs, and digital screens."]
    },
    "Potentiometer": {
        "patterns": ["Potentiometer", "Pot", "Variable Resistor"],
        "responses": ["A potentiometer is a variable resistor with three terminals used to adjust the voltage or resistance in a circuit. It is used for volume controls, tuning, and analog input adjustments."]
    },
    "Relay": {
        "patterns": ["Relay", "Relays"],
        "responses": ["A relay is an electrically operated switch that uses an electromagnet to mechanically control the contacts. It is used for switching high-power loads, motor control, and automation."]
    },
    "Sensor": {
        "patterns": ["Sensor", "Sensors"],
        "responses": ["A sensor is a device that detects and responds to a physical stimulus, converting it into an electrical signal. Sensors are used in measurement, monitoring, control systems, and IoT applications."]
    },
    "Battery": {
        "patterns": ["Battery", "Batteries"],
        "responses": ["A battery is a device that stores chemical energy and converts it into electrical energy. Batteries are used as power sources in electronic devices, portable equipment, and energy storage systems."]
    },
    "Switch": {
        "patterns": ["Switch", "Switches"],
        "responses": ["A switch is a mechanical or electronic device used to interrupt or divert the flow of electric current in a circuit. Switches are used for control, on/off operations, and circuit routing."]
    },
    "Fuse": {
        "patterns": ["Fuse", "Fuses"],
        "responses": ["A fuse is a safety device used to protect electrical circuits from overcurrent and short circuits. Fuses are designed to break the circuit when the current exceeds a predetermined threshold."]
    },
    "Resistor Array": {
        "patterns": ["Resistor Array", "Resistor Network"],
        "responses": ["A resistor array or network is a package of multiple resistors in a single integrated circuit. It is used for precision resistance matching, voltage division, and compact circuit design."]
    },
    "Capacitor Array": {
        "patterns": ["Capacitor Array", "Capacitor Network"],
        "responses": ["A capacitor array or network is a package of multiple capacitors in a single integrated circuit. It is used for filtering, decoupling, and energy storage in compact electronic designs."]
    },
    "Optocoupler": {
        "patterns": ["Optocoupler", "Opto-Isolator"],
        "responses": ["An optocoupler is a component that transfers electrical signals between isolated circuits using light waves. It is used for electrical isolation, noise reduction, and voltage level shifting."]
    },
    "Voltage Divider": {
        "patterns": ["Voltage Divider"],
        "responses": ["A voltage divider is a simple circuit that divides a voltage into smaller parts using resistors. It is used for level shifting, sensor interfacing, and analog signal scaling."]
    },
    "Current Sensor": {
        "patterns": ["Current Sensor"],
        "responses": ["A current sensor is a device that measures electric current flowing through a conductor. It is used for monitoring, protection, and feedback control in power electronics and automation."]
    },

    "Heat Sink": {
        "patterns": ["Heat Sink"],
        "responses": ["A heat sink is a passive component used to dissipate heat from electronic devices, preventing overheating and ensuring optimal performance. Heat sinks are used in CPUs, power transistors, and power supplies."]
    },
    "Voltage Reference": {
        "patterns": ["Voltage Reference"],
        "responses": ["A voltage reference is a precision electronic component that generates a stable voltage output. It is used as a standard voltage source for calibration, measurement, and reference in circuits."]
    },
    "Amplifier": {
        "patterns": ["Amplifier", "Amplifiers"],
        "responses": ["An amplifier is an electronic device that increases the amplitude of a signal. Amplifiers are used in audio systems, RF communication, instrumentation, and signal processing."]
    },
    "Encoder": {
        "patterns": ["Encoder", "Encoders"],
        "responses": ["An encoder is a device that converts motion or position into an electrical signal. Encoders are used in robotics, motor control, navigation systems, and industrial automation."]
    },
    "Decoder": {
        "patterns": ["Decoder", "Decoders"],
        "responses": ["A decoder is a combinational logic circuit that converts binary information into specific outputs. Decoders are used in digital systems, memory addressing, and data processing."]
    },
    "Multiplexer (MUX)": {
        "patterns": ["Multiplexer", "MUX"],
        "responses": ["A multiplexer is a digital circuit that selects one of several input signals and forwards it to a single output. Multiplexers are used in data routing, communication systems, and control applications."]
    },
    "Demultiplexer (DEMUX)": {
        "patterns": ["Demultiplexer", "DEMUX"],
        "responses": ["A demultiplexer is a digital circuit that receives one input and directs it to one of several possible outputs. Demultiplexers are used in data distribution, memory addressing, and signal routing."]
    },
    "Logic Gates": {
        "patterns": ["Logic Gates", "Logic Gate"],
        "responses": ["Logic gates are fundamental building blocks of digital circuits that perform logical operations on binary inputs. They include AND, OR, NOT, NAND, NOR, XOR, and XNOR gates used in Boolean logic."]
    },
    "Power Supply": {
        "patterns": ["Power Supply", "PSU"],
        "responses": ["A power supply is an electronic device that converts electrical power from a source into usable power for electronic circuits. Power supplies include AC/DC converters, linear regulators, and switching regulators."]
    },
    "Clock Generator": {
        "patterns": ["Clock Generator", "Clock IC"],
        "responses": ["A clock generator is an electronic circuit that produces timing signals for digital circuits. Clock generators are used for synchronization, timing control, and frequency generation in microprocessors and systems."]
    },
    "Motor Driver": {
        "patterns": ["Motor Driver", "Motor Controller"],
        "responses": ["A motor driver is an electronic circuit or IC that controls the speed, direction, and operation of electric motors. Motor drivers are used in robotics, automation, and motor control applications."]
    },
    "LCD Driver": {
        "patterns": ["LCD Driver"],
        "responses": ["An LCD driver is an integrated circuit that generates signals to drive liquid crystal displays (LCDs). LCD drivers are used in display modules, graphical interfaces, and embedded systems."]
    },
    "EPROM (Erasable Programmable Read-Only Memory)": {
        "patterns": ["EPROM", "Erasable Programmable Read-Only Memory"],
        "responses": ["An EPROM is a type of non-volatile memory that retains its data even when power is turned off. EPROMs are used for firmware storage, code execution, and configuration settings."]
    },
    "EEPROM (Electrically Erasable Programmable Read-Only Memory)": {
        "patterns": ["EEPROM", "Electrically Erasable Programmable Read-Only Memory"],
        "responses": ["An EEPROM is a non-volatile memory that can be electrically erased and reprogrammed. EEPROMs are used for data storage, parameter settings, and small code storage."]
    },
    "Flash Memory": {
        "patterns": ["Flash Memory"],
        "responses": ["Flash memory is a type of non-volatile computer memory that can be electrically erased and reprogrammed. It is used for firmware storage, data storage, and code execution in microcontrollers."]
    },
    "Voltage Comparator": {
        "patterns": ["Voltage Comparator"],
        "responses": ["A voltage comparator is an electronic circuit that compares two input voltages and indicates which one is larger. Voltage comparators are used in threshold detection, limit setting, and control systems."]
    },
    "Audio Amplifier": {
        "patterns": ["Audio Amplifier"],
        "responses": ["An audio amplifier is an electronic circuit that amplifies audio signals for sound reproduction. Audio amplifiers are used in audio systems, speakers, headphones, and amplification circuits."]
    },
    "RF Transceiver": {
        "patterns": ["RF Transceiver", "Radio Frequency Transceiver"],
        "responses": ["An RF transceiver is a device that combines both transmission and reception functions for radio frequency signals. RF transceivers are used in wireless communication, RF modules, and IoT devices."]
    },
    "Temperature Sensor": {
        "patterns": ["Temperature Sensor", "Thermistor"],
        "responses": ["A temperature sensor is a device that measures temperature and converts it into an electrical signal. Temperature sensors are used in HVAC systems, industrial control, and environmental monitoring."]
    },
    "Humidity Sensor": {
        "patterns": ["Humidity Sensor"],
        "responses": ["A humidity sensor is a device that measures relative humidity in the air and converts it into an electrical signal. Humidity sensors are used in climate control, weather stations, and IoT applications."]
    },
    "Pressure Sensor": {
        "patterns": ["Pressure Sensor"],
        "responses": ["A pressure sensor is a device that measures pressure and converts it into an electrical signal. Pressure sensors are used in automotive systems, industrial automation, and altimeter applications."]
    },
    "Accelerometer": {
        "patterns": ["Accelerometer"],
        "responses": ["An accelerometer is a sensor that measures acceleration and tilt. Accelerometers are used in motion detection, orientation sensing, and inertial navigation systems."]
    },
    "Gyroscope": {
        "patterns": ["Gyroscope"],
        "responses": ["A gyroscope is a sensor that measures angular velocity and orientation. Gyroscopes are used in navigation systems, drones, robotics, and stabilization applications."]
    },
    "Infrared (IR) Sensor": {
        "patterns": ["Infrared Sensor", "IR Sensor"],
        "responses": ["An infrared sensor detects infrared radiation emitted or reflected by objects. IR sensors are used in proximity detection, motion sensing, and remote controls."]
    },
    "Ultrasonic Sensor": {
        "patterns": ["Ultrasonic Sensor"],
        "responses": ["An ultrasonic sensor uses sound waves above the human hearing range to measure distance or detect objects. Ultrasonic sensors are used in robotics, parking systems, and industrial automation."]
    },
    "RFID Reader": {
        "patterns": ["RFID Reader"],
        "responses": ["An RFID reader is a device that wirelessly reads and transmits data stored on RFID tags. RFID readers are used in access control, inventory management, and asset tracking systems."]
    },
    "Piezoelectric Transducer": {
        "patterns": ["Piezoelectric Transducer"],
        "responses": ["A piezoelectric transducer converts mechanical energy into electrical signals or vice versa using the piezoelectric effect. They are used in sensors, actuators, ultrasound devices, and acoustic applications."]
    },
    "IC": {
        "patterns": ["integrated circuit", "IC"],
        "responses": ["An Integrated Circuit (IC) is a miniaturized electronic circuit that contains many interconnected semiconductor devices. ICs are used in computers, smartphones, and various electronic systems."]
    },
    "capacitive sensor": {
        "patterns": ["capacitive sensor", "capacitance sensor"],
        "responses": ["A capacitive sensor measures changes in capacitance to detect proximity or touch. It is used in touchscreens, proximity switches, and position sensors."]
    },
    "oscillator": {
        "patterns": ["oscillator", "oscillators"],
        "responses": ["An oscillator is an electronic circuit that generates periodic waveforms such as sine, square, or sawtooth waves. It is used in clocks, signal generators, and communications systems."]
    },
    "op-amp": {
        "patterns": ["op-amp", "operational amplifier"],
        "responses": ["An Operational Amplifier (op-amp) is a high-gain differential amplifier used for signal conditioning, filtering, and mathematical operations in circuits."]
    },
    "relay": {
        "patterns": ["relay", "relays"],
        "responses": ["A relay is an electrically operated switch that controls a high-power circuit with a low-power signal. It is used in automation, control systems, and power distribution."]
    },
    "microcontroller": {
        "patterns": ["microcontroller", "MCU"],
        "responses": ["A Microcontroller (MCU) is a small computer on a single integrated circuit. It contains a processor, memory, and I/O peripherals. MCUs are used in embedded systems and IoT devices."]
    },
    "voltage regulator": {
        "patterns": ["voltage regulator", "regulator IC"],
        "responses": ["A Voltage Regulator is an electronic circuit that maintains a constant output voltage regardless of input voltage fluctuations. It is used to power sensitive components."]
    },
    "resistor network": {
        "patterns": ["resistor network", "resistor array"],
        "responses": ["A Resistor Network or Resistor Array is a package containing multiple resistors in one component. It simplifies circuit design and saves board space."]
    },
    "capacitor bank": {
        "patterns": ["capacitor bank", "capacitor array"],
        "responses": ["A Capacitor Bank or Capacitor Array is a group of capacitors connected in parallel or series to increase capacitance. It is used for energy storage and power factor correction."]
    },
    "diode bridge": {
        "patterns": ["diode bridge", "bridge rectifier"],
        "responses": ["A Diode Bridge or Bridge Rectifier is a circuit that converts alternating current (AC) to direct current (DC) by using four diodes arranged in a bridge configuration."]
    },
    "transistor array": {
        "patterns": ["transistor array"],
        "responses": ["A Transistor Array is a package containing multiple transistors in one component. It is used in applications requiring multiple amplifiers or switching circuits."]
    },
    "relay module": {
        "patterns": ["relay module"],
        "responses": ["A Relay Module is a circuit board containing one or more relays and associated control electronics. It is used to switch high-power loads with low-power signals."]
    },
    "motor driver": {
        "patterns": ["motor driver", "motor control IC"],
        "responses": ["A Motor Driver or Motor Control IC is an electronic device used to control the speed and direction of electric motors. It is used in robotics, automation, and motor control applications."]
    },
    "LCD display": {
        "patterns": ["LCD display", "liquid crystal display"],
        "responses": ["An LCD Display (Liquid Crystal Display) is a flat-panel display technology that uses liquid crystals to produce images. LCDs are used in monitors, TVs, and digital devices."]
    },
    "sensor module": {
        "patterns": ["sensor module"],
        "responses": ["A Sensor Module is a compact unit containing one or more sensors and signal processing circuits. It is used for environmental monitoring, automation, and IoT applications."]
    },
    "optocoupler": {
        "patterns": ["optocoupler", "opto-isolator"],
        "responses": ["An Optocoupler or Opto-isolator is a device that transfers electrical signals using light waves. It provides electrical isolation between input and output circuits."]
    },
    "crystal oscillator": {
        "patterns": ["crystal oscillator"],
        "responses": ["A Crystal Oscillator is an electronic circuit that generates precise and stable oscillations based on the mechanical resonance of a crystal. It is used in clocks, microcontrollers, and communication systems."]
    },
    "amplifier": {
        "patterns": ["amplifier", "amplifiers"],
        "responses": ["An Amplifier is an electronic device that increases the amplitude of a signal. It is used in audio systems, RF communication, and instrumentation."]
    },
    "logic gate": {
        "patterns": ["logic gate", "logic gates"],
        "responses": ["A Logic Gate is a digital circuit element that performs logical operations (AND, OR, NOT, etc.) on input signals. Logic gates are building blocks of digital circuits."]
    },
    "fuse": {
        "patterns": ["fuse", "fuses"],
        "responses": ["A Fuse is a protective device that interrupts current flow in a circuit when it exceeds a safe level. It is used to prevent damage to components."]
    },
    "varistor": {
        "patterns": ["varistor", "MOV"],
        "responses": ["A Varistor or Metal Oxide Varistor (MOV) is a voltage-dependent resistor used for transient voltage suppression and surge protection in electronic circuits."]
    },
    "potentiometer": {
        "patterns": ["potentiometer", "pot"],
        "responses": ["A Potentiometer (Pot) is a variable resistor used to control voltage or adjust signal levels in circuits. It is commonly used for volume control and tuning."]
    },
    "fuse holder": {
        "patterns": ["fuse holder"],
        "responses": ["A Fuse Holder is a device used to mount and protect fuses in electrical circuits. It provides a secure connection and facilitates easy replacement of fuses."]
    },
    "heat sink": {
        "patterns": ["heat sink"],
        "responses": ["A Heat Sink is a passive cooling device used to dissipate heat from electronic components such as transistors and ICs. It improves thermal performance and prolongs component life."]
    },
    "transformer": {
        "patterns": ["transformer", "power transformer"],
        "responses": ["A Transformer is a device that transfers electrical energy between two or more circuits through electromagnetic induction. It is used for voltage conversion and isolation."]
    },
    "current sensor": {
        "patterns": ["current sensor", "current transducer"],
        "responses": ["A Current Sensor or Current Transducer is a device that measures electric current flowing through a conductor. It is used for monitoring and control in power systems."]
    },
    "photodiode": {
        "patterns": ["photodiode"],
        "responses": ["A Photodiode is a semiconductor device that converts light into electrical current. It is used in optical communication, light sensors, and imaging applications."]
    },
    "piezoelectric buzzer": {
        "patterns": ["piezoelectric buzzer"],
        "responses": ["A Piezoelectric Buzzer is a type of transducer that converts electrical signals into mechanical vibrations, producing sound. It is used in alarms, buzzers, and electronic musical instruments."]
    },
    "connector": {
        "patterns": ["connector", "connectors"],
        "responses": ["A Connector is a mechanical device used to join electrical circuits or components together. It provides a secure and reliable electrical connection."]
    },
    "switch": {
        "patterns": ["switch", "switches"],
        "responses": ["A Switch is an electrical component used to interrupt or divert the flow of current in a circuit. It is used for control and on/off operations."]
    },
    "battery": {
        "patterns": ["battery", "batteries"],
        "responses": ["A Battery is a device that stores chemical energy and converts it into electrical energy. Batteries are used as portable power sources in electronic devices."]
    },
    "fuse box": {
        "patterns": ["fuse box"],
        "responses": ["A Fuse Box is an enclosure that contains multiple fuses or circuit breakers to protect electrical circuits from overcurrent and short circuits. It is commonly used in homes and vehicles."]
    },
    "circuit breaker": {
        "patterns": ["circuit breaker"],
        "responses": ["A Circuit Breaker is an electrical switch designed to protect circuits from overloads and short circuits. It automatically interrupts current flow when abnormal conditions occur."]
    },
    "oscilloscope": {
        "patterns": ["oscilloscope", "scope"],
        "responses": ["An Oscilloscope (Scope) is a test instrument used to visualize and analyze electronic signals over time. It is used for waveform analysis, troubleshooting, and measurements."]
    },
    "multimeter": {
        "patterns": ["multimeter"],
        "responses": ["A Multimeter is a versatile tool used to measure voltage, current, and resistance in electrical circuits. It is essential for troubleshooting and testing."]
    },
    "fuse tester": {
        "patterns": ["fuse tester"],
        "responses": ["A Fuse Tester is a device used to check the continuity and functionality of fuses. It helps in identifying faulty fuses and ensuring circuit protection."]
    },
    "soldering iron": {
        "patterns": ["soldering iron"],
        "responses": ["A Soldering Iron is a tool used for soldering electronic components to circuit boards. It melts solder to create electrical connections."]
    },
    "heat shrink tubing": {
        "patterns": ["heat shrink tubing"],
        "responses": ["Heat Shrink Tubing is a thermoplastic tube that shrinks when heated, providing insulation and protection for wires and components in electronic circuits."]
    },
    "printed circuit board (PCB)": {
        "patterns": ["printed circuit board", "PCB"],
        "responses": ["A Printed Circuit Board (PCB) is a rigid board that connects electronic components through conductive pathways. It provides mechanical support and electrical connections in circuits."]
    },
    "antenna": {
        "patterns": ["antenna", "antennas"],
        "responses": ["An Antenna is a device used to transmit and receive radio waves. It is essential for wireless communication, broadcasting, and RF systems."]
    },
    "grounding wire": {
        "patterns": ["grounding wire"],
        "responses": ["A Grounding Wire is a conductor that connects electrical equipment to the ground or earth. It provides safety by preventing electrical shocks and reducing interference."]
    },
    "thermistor": {
        "patterns": ["thermistor"],
        "responses": ["A Thermistor is a temperature-sensitive resistor used to measure and control temperature in electronic circuits. It is commonly used in temperature sensors and thermal compensation."]
    },
    "speaker": {
        "patterns": ["speaker", "speakers"],
        "responses": ["A Speaker is a transducer that converts electrical signals into sound waves. It is used for audio output in devices such as radios, televisions, and multimedia systems."]
    },
    "motor": {
        "patterns": ["motor", "motors"],
        "responses": ["A Motor is a device that converts electrical energy into mechanical energy, producing motion. It is used in machines, robotics, and automation systems."]
    },
    "encoder": {
        "patterns": ["encoder", "encoders"],
        "responses": ["An Encoder is a device used to convert mechanical position or motion into digital signals. It is used in control systems, robotics, and position sensing applications."]
    },
    "decoder": {
        "patterns": ["decoder", "decoders"],
        "responses": ["A Decoder is a circuit that converts coded information into a form suitable for processing or display. It is used in digital electronics, communications, and computing."]
    },

    "PIC16F877A": {
        "patterns": ["PIC16F877A", "PIC microcontroller"],
        "responses": ["The PIC16F877A is a popular 8-bit microcontroller manufactured by Microchip Technology. It features a wide range of peripherals and is commonly used in embedded systems, industrial control, and automation applications."]
    },
    "NE555 Timer": {
        "patterns": ["NE555 Timer", "555 timer IC"],
        "responses": ["The NE555 Timer is a versatile integrated circuit used for timing and pulse generation. It can be configured in various modes such as astable, monostable, and bistable, making it ideal for timing circuits, oscillators, and PWM generation."]
    },
    "CD4017": {
        "patterns": ["CD4017", "decade counter"],
        "responses": ["The CD4017 is a CMOS decade counter IC capable of counting from 0 to 9 sequentially. It is commonly used in digital clocks, frequency dividers, and sequential LED lighting applications."]
    },
    "LM741": {
        "patterns": ["LM741", "operational amplifier IC"],
        "responses": ["The LM741 is a general-purpose operational amplifier (op-amp) IC known for its high gain, wide frequency response, and versatility. It is used in amplifiers, filters, and signal processing circuits."]
    },
    "LM317": {
        "patterns": ["LM317", "voltage regulator IC"],
        "responses": ["The LM317 is an adjustable voltage regulator IC capable of providing a stable output voltage over a wide range. It is used in power supplies, battery chargers, and voltage reference circuits."]
    },
    "ATmega328": {
        "patterns": ["ATmega328", "AVR microcontroller"],
        "responses": ["The ATmega328 is an 8-bit AVR microcontroller manufactured by Atmel (now Microchip Technology). It is widely used in Arduino boards and various embedded systems for its performance and features."]
    },
    "LM386": {
        "patterns": ["LM386", "audio amplifier IC"],
        "responses": ["The LM386 is a low-voltage audio power amplifier IC capable of delivering amplification to audio signals. It is commonly used in portable devices, audio amplifiers, and small speaker systems."]
    },
    "74HC595": {
        "patterns": ["74HC595", "shift register IC"],
        "responses": ["The 74HC595 is an 8-bit serial-in-parallel-out shift register IC used for data storage and serial-to-parallel conversion. It is commonly used in LED matrix displays, LED drivers, and digital control circuits."]
    },
    "MAX232": {
        "patterns": ["MAX232", "RS232 driver/receiver IC"],
        "responses": ["The MAX232 is a dual driver/receiver IC used for converting TTL/CMOS logic levels to RS232 voltage levels and vice versa. It is used in serial communication interfaces, UARTs, and microcontroller systems."]
    },
    "LM555": {
        "patterns": ["LM555", "555 timer IC"],
        "responses": ["The LM555 is a versatile timer IC used for generating accurate time delays, oscillations, and pulse-width modulation (PWM) signals. It is widely used in timing circuits, pulse generators, and LED flashers."]
    },
    "ATmega2560": {
        "patterns": ["ATmega2560", "AVR microcontroller"],
        "responses": ["The ATmega2560 is a high-performance 8-bit AVR microcontroller with advanced features and large memory capacity. It is used in complex embedded systems, robotics, and automation projects."]
    },
    "HC-SR04": {
        "patterns": ["HC-SR04", "ultrasonic sensor module"],
        "responses": ["The HC-SR04 is an ultrasonic sensor module that measures distance by emitting ultrasonic waves and calculating the time for the waves to return. It is used in robotics, proximity sensors, and distance measuring devices."]
    },
    "DS18B20": {
        "patterns": ["DS18B20", "temperature sensor IC"],
        "responses": ["The DS18B20 is a digital temperature sensor IC capable of measuring temperature with high accuracy and resolution. It is used in temperature monitoring systems, weather stations, and industrial applications."]
    },
    "74HC595": {
        "patterns": ["74HC595", "shift register IC"],
        "responses": ["The 74HC595 is an 8-bit serial-in-parallel-out shift register IC used for data storage and serial-to-parallel conversion. It is commonly used in LED matrix displays, LED drivers, and digital control circuits."]
    },
    "LM358": {
        "patterns": ["LM358", "dual operational amplifier IC"],
        "responses": ["The LM358 is a dual operational amplifier (op-amp) IC with low power consumption and wide voltage range. It is used in audio circuits, comparators, and signal conditioning applications."]
    },
    "CD4017": {
        "patterns": ["CD4017", "decade counter"],
        "responses": ["The CD4017 is a CMOS decade counter IC capable of counting from 0 to 9 sequentially. It is commonly used in digital clocks, frequency dividers, and sequential LED lighting applications."]
    },
    "LM7805": {
        "patterns": ["LM7805", "voltage regulator IC"],
        "responses": ["The LM7805 is a fixed 5V voltage regulator IC capable of providing stable 5V output voltage. It is used in power supplies, voltage regulators, and microcontroller circuits."]
    },
    "ESP8266": {
        "patterns": ["ESP8266", "Wi-Fi module"],
        "responses": ["The ESP8266 is a Wi-Fi module with integrated TCP/IP protocol stack, making it suitable for IoT applications, wireless communication, and network connectivity in embedded systems."]
    },
    "ATtiny85": {
        "patterns": ["ATtiny85", "AVR microcontroller"],
        "responses": ["The ATtiny85 is a low-power 8-bit AVR microcontroller with compact size and rich features. It is used in battery-powered devices, sensors, and small-scale embedded projects."]
    },
    "HC-05": {
        "patterns": ["HC-05", "Bluetooth module"],
        "responses": ["The HC-05 is a Bluetooth module used for wireless communication between devices. It supports serial communication and is commonly used in robotics, IoT, and mobile accessories."]
    },
    "MAX7219": {
        "patterns": ["MAX7219", "LED driver IC"],
        "responses": ["The MAX7219 is a LED driver IC capable of driving up to 64 LEDs in a matrix or 7-segment display configuration. It is used in LED displays, scoreboards, and scrolling text displays."]
    },
    "LM317": {
        "patterns": ["LM317", "voltage regulator IC"],
        "responses": ["The LM317 is an adjustable voltage regulator IC capable of providing a stable output voltage over a wide range. It is used in power supplies, battery chargers, and voltage reference circuits."]
    },
    "ADXL335": {
        "patterns": ["ADXL335", "accelerometer IC"],
        "responses": ["The ADXL335 is a triple-axis accelerometer IC capable of measuring acceleration in three dimensions. It is used in motion sensing, orientation detection, and tilt sensing applications."]
    },
    "LM324": {
        "patterns": ["LM324", "quad operational amplifier IC"],
        "responses": ["The LM324 is a quad operational amplifier (op-amp) IC with low power consumption and high slew rate. It is used in audio circuits, instrumentation, and voltage comparators."]
    },
    "DS1307": {
        "patterns": ["DS1307", "real-time clock IC"],
        "responses": ["The DS1307 is a real-time clock (RTC) IC used for timekeeping in embedded systems. It provides accurate time and date information and is commonly used in alarm systems, data loggers, and timers."]
    },
    "ATmega32": {
        "patterns": ["ATmega32", "AVR microcontroller"],
        "responses": ["The ATmega32 is an advanced 8-bit AVR microcontroller with high performance and versatility. It is used in robotics, automation, and control systems for its features and reliability."]
    },
    "MCP3008": {
        "patterns": ["MCP3008", "ADC IC"],
        "responses": ["The MCP3008 is an 8-channel 10-bit analog-to-digital converter (ADC) IC with SPI interface. It is used for converting analog signals to digital values in microcontroller-based systems."]
    },
    "74HC595": {
        "patterns": ["74HC595", "shift register IC"],
        "responses": ["The 74HC595 is an 8-bit serial-in-parallel-out shift register IC used for data storage and serial-to-parallel conversion. It is commonly used in LED matrix displays, LED drivers, and digital control circuits."]
    },
    "ATmega328P": {
        "patterns": ["ATmega328P", "AVR microcontroller"],
        "responses": ["The ATmega328P is a low-power 8-bit AVR microcontroller with enhanced features and compatibility. It is used in Arduino Uno boards and various embedded systems."]
    },
    "HC-SR501": {
        "patterns": ["HC-SR501", "PIR motion sensor module"],
        "responses": ["The HC-SR501 is a passive infrared (PIR) motion sensor module used for detecting human presence or motion. It is used in security systems, lighting control, and automation projects."]
    },
    "LM3914": {
        "patterns": ["LM3914", "LED driver IC"],
        "responses": ["The LM3914 is a monolithic integrated circuit that drives LED bar graph displays. It is used in VU meters, battery level indicators, and visual monitoring systems."]
    },
    "ATtiny2313": {
        "patterns": ["ATtiny2313", "AVR microcontroller"],
        "responses": ["The ATtiny2313 is an 8-bit AVR microcontroller with low power consumption and compact size. It is used in small-scale embedded systems, sensors, and control applications."]
    },
    "DS3231": {
        "patterns": ["DS3231", "real-time clock IC"],
        "responses": ["The DS3231 is a highly accurate real-time clock (RTC) IC with temperature compensation and battery backup. It is used in precision timekeeping applications, data loggers, and alarm systems."]
    },
    "LM7809": {
        "patterns": ["LM7809", "voltage regulator IC"],
        "responses": ["The LM7809 is a fixed 9V voltage regulator IC capable of providing stable 9V output voltage. It is used in power supplies, voltage regulators, and electronic devices."]
    },
    "ESP32": {
        "patterns": ["ESP32", "Wi-Fi and Bluetooth module"],
        "responses": ["The ESP32 is a powerful Wi-Fi and Bluetooth module with dual-core processors, low power consumption, and rich connectivity options. It is used in IoT projects, wireless communication, and smart devices."]
    },
    "ULN2003": {
        "patterns": ["ULN2003", "Darlington transistor array IC"],
        "responses": ["The ULN2003 is a high-voltage, high-current Darlington transistor array IC used for driving inductive loads such as relays, motors, and solenoids. It is commonly used in motor control circuits and robotics."]
    },
    "MAX232": {
        "patterns": ["MAX232", "RS232 driver/receiver IC"],
        "responses": ["The MAX232 is a dual driver/receiver IC used for converting TTL/CMOS logic levels to RS232 voltage levels and vice versa. It is used in serial communication interfaces, UARTs, and microcontroller systems."]
    },
    "ATtiny13": {
        "patterns": ["ATtiny13", "AVR microcontroller"],
        "responses": ["The ATtiny13 is a low-cost, low-power 8-bit AVR microcontroller suitable for small-scale embedded projects, sensors, and control applications."]
    },
    "LM35": {
        "patterns": ["LM35", "temperature sensor IC"],
        "responses": ["The LM35 is a precision temperature sensor IC capable of providing accurate temperature readings in Celsius. It is used in temperature monitoring systems, weather stations, and HVAC applications."]
    },
    "DS18B20": {
        "patterns": ["DS18B20", "temperature sensor IC"],
        "responses": ["The DS18B20 is a digital temperature sensor IC capable of measuring temperature with high accuracy and resolution. It is used in temperature monitoring systems, weather stations, and industrial applications."]
    },
    "MCP23017": {
        "patterns": ["MCP23017", "GPIO expander IC"],
        "responses": ["The MCP23017 is an I2C-based GPIO expander IC that provides additional input/output ports for microcontrollers. It is used in expanding I/O capabilities in embedded systems and control applications."]
    },
    "LM2596": {
        "patterns": ["LM2596", "voltage regulator IC"],
        "responses": ["The LM2596 is a step-down switching regulator IC capable of converting higher voltage to a lower regulated voltage. It is used in power supplies, battery chargers, and voltage converters."]
    },
    "ADXL345": {
        "patterns": ["ADXL345", "accelerometer IC"],
        "responses": ["The ADXL345 is a triple-axis digital accelerometer IC capable of measuring acceleration in three dimensions with high resolution. It is used in motion detection, robotics, and orientation sensing."]
    },
    "SN74HC595": {
        "patterns": ["SN74HC595", "shift register IC"],
        "responses": ["The SN74HC595 is an 8-bit serial-in-parallel-out shift register IC with high-speed operation and low power consumption. It is used in LED matrix displays, LED drivers, and digital control circuits."]
    },
    "MAX7219": {
        "patterns": ["MAX7219", "LED driver IC"],
        "responses": ["The MAX7219 is a LED driver IC capable of driving up to 64 LEDs in a matrix or 7-segment display configuration. It is used in LED displays, scoreboards, and scrolling text displays."]
    },
    "74LS138": {
        "patterns": ["74LS138", "3-to-8 line decoder IC"],
        "responses": ["The 74LS138 is a 3-to-8 line decoder IC used for decoding and selecting one of eight outputs based on input signals. It is used in address decoding, data routing, and digital logic circuits."]
    },
    "74HC4067": {
        "patterns": ["74HC4067", "multiplexer/demultiplexer IC"],
        "responses": ["The 74HC4067 is a 16-channel analog multiplexer/demultiplexer IC used for signal routing and selection in microcontroller-based systems. It is used in data acquisition, sensor interfacing, and signal processing."]
    },

    "Arduino Uno": {
        "patterns": ["Arduino Uno", "ATmega328P"],
        "responses": ["The Arduino Uno is a popular microcontroller board based on the ATmega328P MCU. It is widely used for prototyping, DIY projects, and educational purposes in the embedded system and IoT community."]
    },
    "Raspberry Pi": {
        "patterns": ["Raspberry Pi", "RPi"],
        "responses": ["The Raspberry Pi is a credit-card-sized single-board computer (SBC) that runs Linux-based operating systems. It is used for a wide range of IoT projects, home automation, media centers, and education."]
    },
    "ESP8266": {
        "patterns": ["ESP8266", "Wi-Fi module"],
        "responses": ["The ESP8266 is a low-cost Wi-Fi module with integrated TCP/IP protocol stack. It is widely used in IoT applications, home automation, remote sensing, and Wi-Fi-connected devices."]
    },
    "ESP32": {
        "patterns": ["ESP32", "Wi-Fi and Bluetooth module"],
        "responses": ["The ESP32 is a powerful Wi-Fi and Bluetooth module with dual-core processors and rich connectivity options. It is used in IoT projects, wearable devices, smart homes, and industrial automation."]
    },
    "Arduino Nano": {
        "patterns": ["Arduino Nano", "ATmega328"],
        "responses": ["The Arduino Nano is a compact-sized microcontroller board based on the ATmega328 MCU. It is used in space-constrained projects, wearable electronics, and embedded systems."]
    },
    "Raspberry Pi Zero": {
        "patterns": ["Raspberry Pi Zero", "RPi Zero"],
        "responses": ["The Raspberry Pi Zero is a smaller and more affordable version of the Raspberry Pi SBC. It is used in compact IoT projects, robotics, and embedded applications."]
    },
    "NodeMCU": {
        "patterns": ["NodeMCU", "ESP8266"],
        "responses": ["The NodeMCU is an open-source IoT platform based on the ESP8266 Wi-Fi module. It is used for IoT prototyping, home automation, sensor networks, and cloud connectivity."]
    },
    "Arduino Mega": {
        "patterns": ["Arduino Mega", "ATmega2560"],
        "responses": ["The Arduino Mega is a microcontroller board based on the ATmega2560 MCU with an expanded set of I/O pins. It is used for projects requiring more I/O, complex automation, and robotics."]
    },
    "Raspberry Pi 4": {
        "patterns": ["Raspberry Pi 4", "RPi 4"],
        "responses": ["The Raspberry Pi 4 is a powerful SBC with improved performance, 4K video support, and USB 3.0 ports. It is used in multimedia applications, IoT gateways, and advanced projects."]
    },
    "Arduino Due": {
        "patterns": ["Arduino Due", "AT91SAM3X8E"],
        "responses": ["The Arduino Due is a microcontroller board based on the Atmel SAM3X8E ARM Cortex-M3 CPU. It is used for high-performance applications, digital signal processing, and real-time control."]
    },
    "Raspberry Pi Pico": {
        "patterns": ["Raspberry Pi Pico", "RPi Pico"],
        "responses": ["The Raspberry Pi Pico is a microcontroller board based on the RP2040 MCU with dual-core ARM Cortex-M0+ processors. It is used in low-power IoT projects, sensors, and wearables."]
    },
    "HC-SR04": {
        "patterns": ["HC-SR04", "ultrasonic sensor module"],
        "responses": ["The HC-SR04 is an ultrasonic sensor module used for distance measurement based on ultrasonic waves. It is used in robotics, proximity detection, and obstacle avoidance systems."]
    },
    "DHT11": {
        "patterns": ["DHT11", "temperature and humidity sensor"],
        "responses": ["The DHT11 is a low-cost digital temperature and humidity sensor module. It is used in weather stations, climate monitoring, and environmental sensing applications."]
    },
    "DHT22": {
        "patterns": ["DHT22", "AM2302"],
        "responses": ["The DHT22 (AM2302) is an advanced version of the DHT11 sensor with higher accuracy and wider temperature/humidity range. It is used in HVAC systems, data loggers, and smart thermostats."]
    },
    "PIR Motion Sensor": {
        "patterns": ["PIR Motion Sensor", "Passive Infrared Sensor"],
        "responses": ["The PIR (Passive Infrared) Motion Sensor detects human movement based on infrared radiation. It is used in security systems, lighting control, and occupancy detection."]
    },
    "MQ-2 Gas Sensor": {
        "patterns": ["MQ-2 Gas Sensor", "gas detection module"],
        "responses": ["The MQ-2 Gas Sensor is used for detecting various gases such as LPG, methane, and smoke. It is used in gas leakage detection systems, air quality monitors, and safety alarms."]
    },
    "MQ-7 Carbon Monoxide Sensor": {
        "patterns": ["MQ-7 Carbon Monoxide Sensor", "CO sensor"],
        "responses": ["The MQ-7 Carbon Monoxide Sensor detects carbon monoxide (CO) gas concentration. It is used in CO alarms, environmental monitoring, and industrial safety systems."]
    },
    "Soil Moisture Sensor": {
        "patterns": ["Soil Moisture Sensor"],
        "responses": ["The Soil Moisture Sensor measures the moisture level in soil for plant irrigation control. It is used in agriculture automation, smart gardening, and moisture monitoring."]
    },
    "IR Sensor": {
        "patterns": ["IR Sensor", "Infrared Sensor"],
        "responses": ["The IR (Infrared) Sensor detects infrared radiation emitted by objects. It is used in motion detection, object tracking, and proximity sensing applications."]
    },
    "HC-SR501": {
        "patterns": ["HC-SR501", "PIR motion sensor module"],
        "responses": ["The HC-SR501 is a PIR (Passive Infrared) motion sensor module used for human presence detection. It is commonly used in security systems, lighting automation, and occupancy sensing."]
    },
    "Rain Sensor": {
        "patterns": ["Rain Sensor", "rain detection module"],
        "responses": ["The Rain Sensor detects rainwater for automated weather-based control systems. It is used in irrigation systems, weather stations, and smart home automation."]
    },
    "Ultrasonic Sensor": {
        "patterns": ["Ultrasonic Sensor"],
        "responses": ["The Ultrasonic Sensor measures distance by sending and receiving ultrasonic waves. It is used in robotics, object detection, and proximity sensing applications."]
    },
    "LM35 Temperature Sensor": {
        "patterns": ["LM35 Temperature Sensor"],
        "responses": ["The LM35 Temperature Sensor is an analog temperature sensor with high accuracy and linear output. It is used in temperature measurement, HVAC systems, and thermal control applications."]
    },
    "PIR Sensor Module": {
        "patterns": ["PIR Sensor Module", "Passive Infrared Sensor"],
        "responses": ["The PIR Sensor Module detects motion based on changes in infrared radiation. It is used in security systems, automatic lighting, and occupancy detection."]
    },
    "IR Obstacle Avoidance Sensor": {
        "patterns": ["IR Obstacle Avoidance Sensor", "infrared sensor module"],
        "responses": ["The IR Obstacle Avoidance Sensor detects obstacles using infrared reflection. It is used in robotics, collision avoidance systems, and smart navigation."]
    },
    "Magnetic Reed Switch": {
        "patterns": ["Magnetic Reed Switch"],
        "responses": ["The Magnetic Reed Switch is used for proximity sensing based on magnetic fields. It is used in door/window alarms, security systems, and industrial automation."]
    },
    "Flex Sensor": {
        "patterns": ["Flex Sensor", "flexible bend sensor"],
        "responses": ["The Flex Sensor measures bending or flexing in applications such as robotics, wearable devices, and gesture recognition systems."]
    },
    "PIR Human Body Detection Sensor": {
        "patterns": ["PIR Human Body Detection Sensor"],
        "responses": ["The PIR Human Body Detection Sensor detects human presence based on body heat. It is used in security systems, smart lighting, and occupancy detection."]
    },
    "LDR Sensor": {
        "patterns": ["LDR Sensor", "Light Dependent Resistor"],
        "responses": ["The LDR (Light Dependent Resistor) Sensor measures light intensity. It is used in automatic streetlights, photography, and light level monitoring."]
    },
    "Smoke Detector Sensor": {
        "patterns": ["Smoke Detector Sensor"],
        "responses": ["The Smoke Detector Sensor detects smoke particles in the air for fire alarm systems and safety applications."]
    },
    "Gas Sensor Module": {
        "patterns": ["Gas Sensor Module"],
        "responses": ["The Gas Sensor Module detects various gases such as methane, propane, and carbon monoxide. It is used in gas leak detection, air quality monitoring, and safety alarms."]
    },
    "Water Level Sensor": {
        "patterns": ["Water Level Sensor"],
        "responses": ["The Water Level Sensor measures the level of water in tanks, reservoirs, or containers. It is used in water management systems, automatic irrigation, and liquid level control."]
    },
    "Humidity Sensor": {
        "patterns": ["Humidity Sensor"],
        "responses": ["The Humidity Sensor measures relative humidity in the air. It is used in weather stations, HVAC systems, and environmental monitoring."]
    },
    "Accelerometer Sensor": {
        "patterns": ["Accelerometer Sensor"],
        "responses": ["The Accelerometer Sensor measures acceleration in three dimensions. It is used in motion sensing, tilt detection, and vibration analysis."]
    },
    "Pressure Sensor": {
        "patterns": ["Pressure Sensor"],
        "responses": ["The Pressure Sensor measures atmospheric pressure or fluid pressure. It is used in barometers, altimeters, and industrial pressure measurement."]
    },
    "Temperature Sensor": {
        "patterns": ["Temperature Sensor"],
        "responses": ["The Temperature Sensor measures ambient temperature. It is used in HVAC systems, weather stations, and thermal management."]
    },
    "Proximity Sensor": {
        "patterns": ["Proximity Sensor"],
        "responses": ["The Proximity Sensor detects the presence or absence of an object in close proximity. It is used in touchless switches, robotics, and security systems."]
    },
    "IR Flame Sensor": {
        "patterns": ["IR Flame Sensor", "flame detection module"],
        "responses": ["The IR Flame Sensor detects flames or fire based on infrared radiation. It is used in fire alarm systems, flame detection, and safety applications."]
    },
    "Touch Sensor": {
        "patterns": ["Touch Sensor", "capacitive touch sensor"],
        "responses": ["The Touch Sensor detects touch or proximity without physical contact. It is used in touchscreens, user interfaces, and interactive displays."]
    },
    "Vibration Sensor": {
        "patterns": ["Vibration Sensor"],
        "responses": ["The Vibration Sensor detects vibrations or shocks in machinery or structures. It is used in condition monitoring, seismic detection, and alarm systems."]
    },
    "Color Sensor": {
        "patterns": ["Color Sensor"],
        "responses": ["The Color Sensor measures color properties such as RGB values or color temperature. It is used in color detection, color sorting, and display calibration."]
    },
    "UV Sensor": {
        "patterns": ["UV Sensor", "Ultraviolet Sensor"],
        "responses": ["The UV Sensor measures ultraviolet (UV) radiation levels. It is used in UV index measurement, skin protection devices, and environmental monitoring."]
    },
    "Sound Sensor": {
        "patterns": ["Sound Sensor"],
        "responses": ["The Sound Sensor detects sound or noise levels. It is used in noise monitoring, smart audio devices, and security systems."]
    },
    "Motion Detector Sensor": {
        "patterns": ["Motion Detector Sensor"],
        "responses": ["The Motion Detector Sensor detects movement or changes in position. It is used in security systems, automatic lighting, and occupancy sensing."]
    },
    "Raindrop Sensor": {
        "patterns": ["Raindrop Sensor"],
        "responses": ["The Raindrop Sensor detects rainwater or water droplets. It is used in rain detection systems, weather stations, and automatic wipers."]
    },
    "IR Receiver Module": {
        "patterns": ["IR Receiver Module", "infrared receiver"],
        "responses": ["The IR Receiver Module receives infrared signals from remote controls or transmitters. It is used in remote control systems, IR communication, and smart devices."]
    },
    "Gas Leakage Sensor": {
        "patterns": ["Gas Leakage Sensor"],
        "responses": ["The Gas Leakage Sensor detects leaks of gas such as LPG or methane. It is used in gas detection systems, safety alarms, and industrial monitoring."]
    },
    "Hall Effect Sensor": {
        "patterns": ["Hall Effect Sensor"],
        "responses": ["The Hall Effect Sensor detects magnetic fields. It is used in speed sensing, position detection, and proximity switches."]
    },
    "IR Proximity Sensor": {
        "patterns": ["IR Proximity Sensor"],
        "responses": ["The IR Proximity Sensor detects objects or obstacles based on infrared reflection. It is used in robotics, motion detection, and object tracking."]
    },
    "Load Cell Sensor": {
        "patterns": ["Load Cell Sensor"],
        "responses": ["The Load Cell Sensor measures weight or force. It is used in weighing scales, force measurement, and industrial automation."]
    },

    "ATtiny85": {
        "patterns": ["ATtiny85", "AVR microcontroller"],
        "responses": ["The ATtiny85 is a low-power 8-bit AVR microcontroller with compact size and versatile I/O capabilities. It is used in small-scale embedded projects, sensors, and low-power applications."]
    },
    "STM32": {
        "patterns": ["STM32", "ARM Cortex-M microcontroller"],
        "responses": ["The STM32 is a family of ARM Cortex-M based microcontrollers known for their high performance and extensive peripheral support. They are used in robotics, IoT devices, and industrial control."]
    },
    "Node-RED": {
        "patterns": ["Node-RED"],
        "responses": ["Node-RED is a flow-based programming platform for IoT applications. It simplifies the integration of devices, APIs, and services in IoT projects."]
    },
    "PIC16F877A": {
        "patterns": ["PIC16F877A", "PIC microcontroller"],
        "responses": ["The PIC16F877A is a popular 8-bit PIC microcontroller known for its versatility and ease of use. It is used in automation, control systems, and consumer electronics."]
    },
    "BeagleBone Black": {
        "patterns": ["BeagleBone Black"],
        "responses": ["The BeagleBone Black is a single-board computer (SBC) based on the ARM Cortex-A8 processor. It is used in IoT development, robotics, and embedded Linux projects."]
    },
    "Adafruit Feather": {
        "patterns": ["Adafruit Feather"],
        "responses": ["The Adafruit Feather is a series of compact development boards with built-in connectivity options such as Wi-Fi, Bluetooth, and LoRa. They are used in portable IoT projects, wearables, and data loggers."]
    },
    "Particle Photon": {
        "patterns": ["Particle Photon"],
        "responses": ["The Particle Photon is a Wi-Fi enabled microcontroller board designed for IoT applications. It is used in cloud-connected projects, remote monitoring, and automation."]
    },
    "ESP8285": {
        "patterns": ["ESP8285"],
        "responses": ["The ESP8285 is a compact version of the ESP8266 Wi-Fi module with integrated flash memory. It is used in space-constrained IoT devices, smart home products, and sensors."]
    },
    "STM8": {
        "patterns": ["STM8", "8-bit microcontroller"],
        "responses": ["The STM8 is an 8-bit microcontroller family known for its cost-effectiveness and low-power operation. It is used in automotive electronics, consumer appliances, and industrial control."]
    },
    "Adafruit Huzzah": {
        "patterns": ["Adafruit Huzzah"],
        "responses": ["The Adafruit Huzzah is an ESP8266-based development board with built-in Wi-Fi connectivity. It is used in IoT prototypes, smart devices, and home automation."]
    },
    "Particle Electron": {
        "patterns": ["Particle Electron"],
        "responses": ["The Particle Electron is a cellular IoT development board with global connectivity. It is used in remote monitoring, asset tracking, and IoT applications without Wi-Fi access."]
    },
    "STM32F4": {
        "patterns": ["STM32F4", "ARM Cortex-M4 microcontroller"],
        "responses": ["The STM32F4 is an ARM Cortex-M4 based microcontroller with DSP and FPU capabilities. It is used in high-performance applications, digital signal processing, and motor control."]
    },
    "Intel Edison": {
        "patterns": ["Intel Edison"],
        "responses": ["The Intel Edison is a compute module for IoT and embedded applications. It offers dual-core processing, Wi-Fi, Bluetooth, and various expansion options."]
    },
    "Nordic nRF52": {
        "patterns": ["Nordic nRF52", "Bluetooth Low Energy (BLE) microcontroller"],
        "responses": ["The Nordic nRF52 series are BLE-enabled microcontrollers with low power consumption and advanced wireless features. They are used in wearables, beacons, and IoT devices."]
    },
    "Texas Instruments MSP430": {
        "patterns": ["Texas Instruments MSP430", "ultra-low-power microcontroller"],
        "responses": ["The Texas Instruments MSP430 is an ultra-low-power microcontroller suitable for battery-operated IoT devices, sensor nodes, and energy-efficient applications."]
    },
    "Cypress PSoC": {
        "patterns": ["Cypress PSoC", "Programmable System-on-Chip"],
        "responses": ["The Cypress PSoC (Programmable System-on-Chip) integrates microcontroller and programmable analog/digital blocks. It is used in mixed-signal IoT applications, sensor interfaces, and control systems."]
    },
    "Teensy": {
        "patterns": ["Teensy"],
        "responses": ["Teensy boards are compact microcontroller platforms with Arduino compatibility and high-performance features. They are used in USB-based projects, audio applications, and HID devices."]
    },
    "Adafruit Trinket": {
        "patterns": ["Adafruit Trinket"],
        "responses": ["The Adafruit Trinket is a small-sized microcontroller board ideal for wearables, LED projects, and compact IoT applications."]
    },
    "Raspberry Pi Compute Module": {
        "patterns": ["Raspberry Pi Compute Module", "RPi Compute Module"],
        "responses": ["The Raspberry Pi Compute Module is a compact version of the Raspberry Pi for embedded applications. It is used in custom PCB designs, industrial automation, and IoT gateways."]
    },
    "Particle Argon": {
        "patterns": ["Particle Argon"],
        "responses": ["The Particle Argon is a Wi-Fi and BLE enabled development board for IoT projects. It is used in mesh networking, cloud connectivity, and smart home applications."]
    },
    "Heltec ESP32 LoRa": {
        "patterns": ["Heltec ESP32 LoRa", "LoRaWAN module"],
        "responses": ["The Heltec ESP32 LoRa module combines ESP32 with LoRaWAN connectivity for long-range IoT applications. It is used in smart agriculture, asset tracking, and remote sensing."]
    },
    "Pycom FiPy": {
        "patterns": ["Pycom FiPy"],
        "responses": ["The Pycom FiPy is a multi-network IoT development board supporting Wi-Fi, BLE, LoRa, Sigfox, and LTE-M/NB-IoT. It is used in versatile IoT projects requiring multiple connectivity options."]
    },
    "Particle Boron": {
        "patterns": ["Particle Boron"],
        "responses": ["The Particle Boron is a cellular IoT development board supporting LTE Cat-M1 and NB-IoT connectivity. It is used in global IoT deployments, asset tracking, and remote monitoring."]
    },
    "NodeMCU ESP32": {
        "patterns": ["NodeMCU ESP32"],
        "responses": ["The NodeMCU ESP32 is a development board based on the ESP32 microcontroller with integrated Wi-Fi and Bluetooth. It is used in IoT prototyping, automation, and sensor networks."]
    },
    "Adafruit ItsyBitsy": {
        "patterns": ["Adafruit ItsyBitsy"],
        "responses": ["The Adafruit ItsyBitsy is a small-sized microcontroller board with various models based on different MCU families. It is used in compact IoT projects, wearables, and robotics."]
    },
    "Espressif ESP32-C3": {
        "patterns": ["Espressif ESP32-C3"],
        "responses": ["The Espressif ESP32-C3 is a low-cost Wi-Fi and Bluetooth microcontroller with RISC-V architecture. It is used in IoT devices, wearables, and smart home products."]
    },
    "STM32L4": {
        "patterns": ["STM32L4", "ARM Cortex-M4 microcontroller"],
        "responses": ["The STM32L4 is an ultra-low-power ARM Cortex-M4 microcontroller with rich features for IoT applications, sensor hubs, and battery-operated devices."]
    },
    "NXP LPC": {
        "patterns": ["NXP LPC", "ARM microcontroller"],
        "responses": ["The NXP LPC series offers ARM-based microcontrollers with high performance and integrated peripherals. They are used in automotive electronics, industrial automation, and IoT gateways."]
    },
    "Adafruit Grand Central M4": {
        "patterns": ["Adafruit Grand Central M4"],
        "responses": ["The Adafruit Grand Central M4 is a powerful microcontroller board based on the SAMD51 MCU. It is used in high-performance IoT projects, robotics, and data logging applications."]
    },
    "ESP32-CAM": {
        "patterns": ["ESP32-CAM", "ESP32 Camera Module"],
        "responses": ["The ESP32-CAM is a development board with ESP32 and camera module for IoT projects, surveillance systems, and video streaming applications."]
    },
    "STM32H7": {
        "patterns": ["STM32H7", "ARM Cortex-M7 microcontroller"],
        "responses": ["The STM32H7 is an advanced ARM Cortex-M7 microcontroller with high performance and DSP capabilities. It is used in real-time control, audio processing, and multimedia applications."]
    },
    "Particle Xenon": {
        "patterns": ["Particle Xenon"],
        "responses": ["The Particle Xenon is a mesh-enabled BLE development board for IoT applications. It is used in sensor networks, smart lighting, and distributed IoT systems."]
    },
    "Pycom GPy": {
        "patterns": ["Pycom GPy"],
        "responses": ["The Pycom GPy is a cellular and Wi-Fi enabled development board supporting LTE Cat-M1, NB-IoT, and global GSM networks. It is used in IoT deployments requiring cellular connectivity."]
    },
    "Nordic nRF52840": {
        "patterns": ["Nordic nRF52840", "Bluetooth 5 microcontroller"],
        "responses": ["The Nordic nRF52840 is a BLE 5-enabled microcontroller with advanced features for IoT, wearables, and wireless connectivity applications."]
    },
    "Adafruit Circuit Playground": {
        "patterns": ["Adafruit Circuit Playground"],
        "responses": ["The Adafruit Circuit Playground is an educational microcontroller board with built-in sensors, LEDs, and buttons. It is used in STEM education, beginner projects, and interactive learning."]
    },
    "Heltec ESP32 OLED": {
        "patterns": ["Heltec ESP32 OLED"],
        "responses": ["The Heltec ESP32 OLED board combines ESP32 with OLED display for IoT projects requiring visual feedback, data logging, and user interaction."]
    },
    "STMicroelectronics Blue Pill": {
        "patterns": ["STMicroelectronics Blue Pill", "STM32F103C8T6"],
        "responses": ["The STMicroelectronics Blue Pill is a low-cost STM32 development board used in embedded projects, automation, and IoT prototyping."]
    },
    "Espressif ESP32-S2": {
        "patterns": ["Espressif ESP32-S2"],
        "responses": ["The Espressif ESP32-S2 is a low-power Wi-Fi microcontroller with enhanced security features. It is used in battery-operated IoT devices, smart home products, and automation."]
    },
    "Raspberry Pi Pico RP2040": {
        "patterns": ["Raspberry Pi Pico RP2040"],
        "responses": ["The Raspberry Pi Pico RP2040 is a microcontroller board with RP2040 MCU designed for IoT, automation, and digital projects."]
    },
    "Adafruit CLUE": {
        "patterns": ["Adafruit CLUE"],
        "responses": ["The Adafruit CLUE is a microcontroller board with various sensors and a color display. It is used in IoT projects, wearable tech, and environmental sensing."]
    },
    "STM32F7": {
        "patterns": ["STM32F7", "ARM Cortex-M7 microcontroller"],
        "responses": ["The STM32F7 is a high-performance ARM Cortex-M7 microcontroller with advanced features for IoT applications, graphical user interfaces, and multimedia systems."]
    },
    "ESP32-SOLO-1": {
        "patterns": ["ESP32-SOLO-1"],
        "responses": ["The ESP32-SOLO-1 is a single-core version of the ESP32 microcontroller with Wi-Fi and Bluetooth connectivity. It is used in IoT devices, smart gadgets, and industrial automation."]
    },
    "Adafruit Metro": {
        "patterns": ["Adafruit Metro"],
        "responses": ["The Adafruit Metro is a series of Arduino-compatible development boards with enhanced features for IoT, automation, and electronics projects."]
    },
    "Raspberry Pi Zero W": {
        "patterns": ["Raspberry Pi Zero W"],
        "responses": ["The Raspberry Pi Zero W is a compact SBC with built-in Wi-Fi and Bluetooth. It is used in IoT applications, robotics, and embedded systems."]
    },
    "Microchip SAMD21": {
        "patterns": ["Microchip SAMD21", "ARM Cortex-M0+ microcontroller"],
        "responses": ["The Microchip SAMD21 is an ARM Cortex-M0+ microcontroller known for its low power consumption and high performance. It is used in IoT, wearables, and battery-operated devices."]
    },
    "ESP32-S2-Kaluga-1 Kit": {
        "patterns": ["ESP32-S2-Kaluga-1 Kit"],
        "responses": ["The ESP32-S2-Kaluga-1 Kit is a development board based on ESP32-S2 with LCD display and various sensors. It is used in IoT prototyping, smart displays, and embedded projects."]
    },
    "Adafruit QT Py": {
        "patterns": ["Adafruit QT Py"],
        "responses": ["The Adafruit QT Py is a tiny microcontroller board with USB-C connectivity, suitable for IoT, wearables, and small-scale projects."]
    },
    "STMicroelectronics Nucleo": {
        "patterns": ["STMicroelectronics Nucleo", "STM32 Nucleo"],
        "responses": ["The STMicroelectronics Nucleo series provides STM32 development boards with Arduino compatibility for IoT, embedded systems, and educational purposes."]
    },
    "Espressif ESP32-WROOM": {
        "patterns": ["Espressif ESP32-WROOM"],
        "responses": ["The Espressif ESP32-WROOM module is a Wi-Fi and Bluetooth enabled solution for IoT devices, smart home products, and industrial automation."]
    },
    "Arduino MKR GSM 1400": {
        "patterns": ["Arduino MKR GSM 1400"],
        "responses": ["The Arduino MKR GSM 1400 is an IoT development board with GSM connectivity for remote monitoring, asset tracking, and global IoT deployments."]
    },
    "Nordic nRF9160": {
        "patterns": ["Nordic nRF9160", "LTE-M/NB-IoT module"],
        "responses": ["The Nordic nRF9160 is a compact LTE-M/NB-IoT module for cellular IoT applications, asset tracking, and remote sensor networks."]
    },
    "Adafruit MagTag": {
        "patterns": ["Adafruit MagTag"],
        "responses": ["The Adafruit MagTag is a low-power eInk display board for IoT projects, weather stations, and information displays."]
    },
    "STM32G4": {
        "patterns": ["STM32G4", "ARM Cortex-M4 microcontroller"],
        "responses": ["The STM32G4 is an ARM Cortex-M4 microcontroller optimized for real-time control, motor control, and IoT applications."]
    },
    "ESP32-S3": {
        "patterns": ["ESP32-S3"],
        "responses": ["The ESP32-S3 is an advanced Wi-Fi and Bluetooth microcontroller with AI capabilities, suitable for IoT, automation, and smart devices."]
    },
    "Particle Tracker": {
        "patterns": ["Particle Tracker"],
        "responses": ["The Particle Tracker is a global asset tracking module with GNSS, cellular connectivity, and long battery life. It is used in logistics, fleet management, and IoT tracking applications."]
    },
    "Heltec ESP8266": {
        "patterns": ["Heltec ESP8266"],
        "responses": ["The Heltec ESP8266 is a compact Wi-Fi module with integrated microcontroller, used in IoT devices, smart home products, and automation projects."]
    },
    "Raspberry Pi 4 Model B": {
        "patterns": ["Raspberry Pi 4 Model B"],
        "responses": ["The Raspberry Pi 4 Model B is a powerful SBC for IoT, media centers, robotics, and educational purposes."]
    },
    "Adafruit Metro M4": {
        "patterns": ["Adafruit Metro M4"],
        "responses": ["The Adafruit Metro M4 is a high-performance microcontroller board based on the SAMD51 MCU, suitable for IoT, automation, and data-intensive applications."]
    },
    "STM32WB": {
        "patterns": ["STM32WB", "Wireless microcontroller"],
        "responses": ["The STM32WB is a wireless microcontroller with dual-core ARM Cortex-M4 and M0+ processors, Bluetooth, and Zigbee support. It is used in IoT devices, wearables, and smart home products."]
    },
    "ESP8266 NodeMCU": {
        "patterns": ["ESP8266 NodeMCU"],
        "responses": ["The ESP8266 NodeMCU is a popular development board with built-in Wi-Fi, used in IoT projects, home automation, and sensor networks."]
    },
    "Adafruit Metro M0 Express": {
        "patterns": ["Adafruit Metro M0 Express"],
        "responses": ["The Adafruit Metro M0 Express is a beginner-friendly microcontroller board for IoT, education, and hobbyist projects."]
    },
    "STMicroelectronics BlueNRG": {
        "patterns": ["STMicroelectronics BlueNRG", "Bluetooth Low Energy (BLE) module"],
        "responses": ["The STMicroelectronics BlueNRG is a BLE module for low-power IoT applications, wearable devices, and wireless sensors."]
    },
    "Raspberry Pi Compute Module 4": {
        "patterns": ["Raspberry Pi Compute Module 4", "RPi Compute Module 4"],
        "responses": ["The Raspberry Pi Compute Module 4 is a compact version of Raspberry Pi 4 designed for industrial IoT, embedded systems, and custom PCB designs."]
    },
    "Adafruit ItsyBitsy M4": {
        "patterns": ["Adafruit ItsyBitsy M4"],
        "responses": ["The Adafruit ItsyBitsy M4 is a compact microcontroller board based on the SAMD51 MCU, used in IoT, robotics, and interactive projects."]
    },
    "ESP32 DevKit": {
        "patterns": ["ESP32 DevKit"],
        "responses": ["The ESP32 DevKit is a development board with ESP32 Wi-Fi and Bluetooth SoC, suitable for IoT, automation, and smart devices."]
    },
    "Particle Argon LTE": {
        "patterns": ["Particle Argon LTE"],
        "responses": ["The Particle Argon LTE is a cellular IoT board with LTE Cat-M1 connectivity, used in remote monitoring, asset tracking, and industrial automation."]
    },
    "Heltec ESP32-CAM": {
        "patterns": ["Heltec ESP32-CAM"],
        "responses": ["The Heltec ESP32-CAM is a development board with ESP32 and camera module, used in surveillance systems, IoT cameras, and video streaming applications."]
    },
    "Raspberry Pi 3 Model B+": {
        "patterns": ["Raspberry Pi 3 Model B+"],
        "responses": ["The Raspberry Pi 3 Model B+ is an SBC with Wi-Fi, Bluetooth, and enhanced performance for IoT, media centers, and robotics."]
    },
    "Adafruit Feather M0 Express": {
        "patterns": ["Adafruit Feather M0 Express"],
        "responses": ["The Adafruit Feather M0 Express is a portable microcontroller board for IoT, wearables, and data logging projects."]
    },
    "STM32L0": {
        "patterns": ["STM32L0", "Ultra-low-power microcontroller"],
        "responses": ["The STM32L0 series is known for its ultra-low-power consumption, making it ideal for battery-operated IoT devices, sensors, and wearables."]
    },
    "Espressif ESP32-C6": {
        "patterns": ["Espressif ESP32-C6"],
        "responses": ["The Espressif ESP32-C6 is a Wi-Fi and Bluetooth microcontroller with dual-core RISC-V processors, suitable for IoT, smart home, and automation applications."]
    },
    "Particle Tracker SoM": {
        "patterns": ["Particle Tracker SoM", "System-on-Module"],
        "responses": ["The Particle Tracker SoM is a cellular SoM with GNSS, LTE Cat-M1, and global connectivity for IoT applications, asset tracking, and logistics."]
    },
    "Heltec LoRa Node": {
        "patterns": ["Heltec LoRa Node"],
        "responses": ["The Heltec LoRa Node is a compact board with LoRaWAN connectivity for long-range IoT applications, smart agriculture, and environmental monitoring."]
    },
    "Raspberry Pi Zero WH": {
        "patterns": ["Raspberry Pi Zero WH"],
        "responses": ["The Raspberry Pi Zero WH is a variant of Pi Zero with pre-soldered GPIO headers, used in IoT projects, educational kits, and embedded systems."]
    },
    "Adafruit QT Py RP2040": {
        "patterns": ["Adafruit QT Py RP2040"],
        "responses": ["The Adafruit QT Py RP2040 is a small-sized microcontroller board with RP2040 MCU, suitable for IoT, wearables, and compact projects."]
    },
    "STMicroelectronics STM8": {
        "patterns": ["STMicroelectronics STM8", "8-bit microcontroller"],
        "responses": ["The STMicroelectronics STM8 is an 8-bit microcontroller series with rich peripherals, used in automotive, industrial, and consumer electronics."]
    },
    "ESP32-S2-WROVER": {
        "patterns": ["ESP32-S2-WROVER"],
        "responses": ["The ESP32-S2-WROVER is an ESP32-S2 module with external PSRAM, used in IoT devices, wearables, and smart home applications."]
    },
    "Adafruit HUZZAH32": {
        "patterns": ["Adafruit HUZZAH32"],
        "responses": ["The Adafruit HUZZAH32 is a ESP32-based development board with Wi-Fi and Bluetooth, used in IoT, home automation, and robotics."]
    },
    "Raspberry Pi Pico with Headers": {
        "patterns": ["Raspberry Pi Pico with Headers"],
        "responses": ["The Raspberry Pi Pico with Headers is a variant of Pico with pre-soldered headers, suitable for IoT, education, and embedded projects."]
    },    
    "important_websites_response": {
        "patterns": ["important websites for electronics engineers"],
        "responses": ["As an electronics engineer, you may find the following websites very useful:\n1. Stack Overflow (https://stackoverflow.com/) - For programming and technical queries\n2. GitHub (https://github.com/) - For version control, collaboration, and open-source projects\n3. IEEE Xplore (https://ieeexplore.ieee.org/) - For accessing research papers and technical publications\n4. Electronics-Lab (https://www.electronics-lab.com/) - For electronics projects, tutorials, and forums\n5. Hackaday (https://hackaday.com/) - For electronics projects, news, and DIY community\n6. All About Circuits (https://www.allaboutcircuits.com/) - For electronics tutorials, articles, and forums\n7. EEWeb (https://www.eeweb.com/) - For electronics news, forums, and resources\n8. Electronics Point (https://www.electronicspoint.com/) - For electronics discussions, tutorials, and resources\n9. EDN Network (https://www.edn.com/) - For electronics design, news, and industry insights\n10. Circuit Digest (https://circuitdigest.com/) - For electronics projects, tutorials, and resources\n11. Hackster.io (https://www.hackster.io/) - For electronics projects, tutorials, and community\n12. SparkFun Electronics (https://www.sparkfun.com/) - For electronics components, kits, and resources\n13. Arduino (https://www.arduino.cc/) - For Arduino development, tutorials, and projects\n14. Raspberry Pi (https://www.raspberrypi.org/) - For Raspberry Pi development, projects, and resources\n15. Digi-Key Electronics (https://www.digikey.com/) - For electronics components, tools, and resources\n16. Mouser Electronics (https://www.mouser.com/) - For electronics components, tools, and resources\n17. Adafruit Industries (https://www.adafruit.com/) - For electronics components, tutorials, and projects\n18. Electronut Labs (https://www.electronut.in/) - For IoT, embedded systems, and electronics projects\n19. Electronics For You (https://electronicsforu.com/) - For electronics news, articles, and tutorials\n20. Engineering.com (https://www.engineering.com/) - For engineering news, articles, and resources\n21. CircuitMaker (https://circuitmaker.com/) - For PCB design, collaboration, and community\n22. PCBWay (https://www.pcbway.com/) - For PCB manufacturing services and resources\n23. Instructables (https://www.instructables.com/) - For DIY projects, tutorials, and community\n24. Element14 (https://www.element14.com/) - For electronics components, tools, and resources\n25. Electromaker (https://www.electromaker.io/) - For electronics projects, tutorials, and community\nThese websites cover a wide range of topics and resources for electronics engineers, from programming and design to projects, components, and industry insights."]
    },
    "useful_applications_response": {
        "patterns": ["useful applications for electronics engineer"],
        "responses": ["As an electronics engineer, you may find the following applications very useful:\n1. Circuit Design and Simulation Tools (e.g., LTspice, PSpice, KiCad)\n2. PCB Design Software (e.g., Altium Designer, Eagle, OrCAD)\n3. Microcontroller Programming IDEs (e.g., Arduino IDE, MPLAB X, Keil µVision)\n4. Signal Processing and Analysis Software (e.g., MATLAB, LabVIEW)\n5. Electronic Component Datasheet Libraries (e.g., Digi-Key, Mouser)\n6. RF Design and Simulation Tools (e.g., ADS, CST Studio Suite, HFSS)\n7. Power Electronics Simulation Software (e.g., PSIM, PLECS)\n8. CAD/CAM Software for Mechanical Design (e.g., SolidWorks, AutoCAD)\n9. Embedded Systems Development Platforms (e.g., Raspberry Pi, BeagleBone)\n10. Industrial Automation Software (e.g., PLC Programming Software, SCADA Systems)\n11. Electronic Circuit Analysis Tools (e.g., SPICE, Multisim)\n12. 3D Printing and Prototyping Software (e.g., Ultimaker Cura, Tinkercad)\n13. FPGA Design and Development Tools (e.g., Xilinx Vivado, Intel Quartus Prime)\n14. Electronic Test and Measurement Equipment (e.g., Oscilloscopes, Multimeters, Function Generators)\n15. IoT Development Platforms (e.g., Arduino IoT Cloud, AWS IoT, Google Cloud IoT)\n16. CAD Libraries for Standard Components (e.g., SnapEDA, Ultra Librarian)\n17. Electronic Design Automation (EDA) Suites (e.g., Cadence, Synopsys, Mentor Graphics)\n18. Thermal Analysis Software for Electronics (e.g., ANSYS Icepak, FloTHERM)\n19. Electronic Manufacturing and Assembly Tools (e.g., Pick and Place Machines, Soldering Stations)\n20. Component Sourcing and Supply Chain Management Tools (e.g., Octopart, Sourcengine)\n21. Antenna Design and Optimization Software (e.g., ANSYS HFSS, CST Antenna Magus)\n22. Electronic CAD Libraries for Symbols and Footprints (e.g., Ultra Librarian, SamacSys)\n23. Augmented Reality (AR) and Virtual Reality (VR) Development Tools for Electronics\n24. Electromagnetic Compatibility (EMC) Testing Software (e.g., EMC Studio, EMCoS Antenna)\n25. Electronic Documentation and Collaboration Platforms (e.g., Altium 365, GitHub for Hardware Projects)\nThese applications cover a wide range of tasks and specialties in electronics engineering, from circuit design and simulation to prototyping, testing, and manufacturing."]
    }
    }

