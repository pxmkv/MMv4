

Kicad Practiceeeeeeeee

Opening Kicad
- Open project not individual files
- Make sure you have the extra parts downloaded from Github
- PS: You can only have one project open per instance of Kicad

Schematic
- Controls easier with a mouse
- Symbol corresponds to a part
- Symbols have pins/ports
- Kicad is not very smart
- Symbols you can get from Kicad internal library, Digikey library, random online sources such as Github, or you can make your own
- you open up a datasheet and make your own based off it
- the important thing is the pin type, which is what Kicad uses to determine what you wanted the pin for, but if it's an existing symbol there's already those settings preset
- W is for wire, that allows you to connect pins
- Bus allows you to groups wires
- Labels - allows you to not use wires - L
- The X means no connect
- So if you wanted a power rail, you would use a Power Flag
- And you want to use GND flags for ground
- What if you wanted say 2.45V? I think you would use a label but it'd be good tolook up
- Basic rules: GND bottom, Pwr up, signals left to right
- A for placing symbols
- For small components, often they have a single letter designation
- such as R, C...
- Double click to set value
- Before you do anything else, you annotate schematic
- But before you finish, run electrical rules check
- Might need to put power flags to indicate to Kicad what your power rails are for the sole purpose of getting that green check on the electrical rules check
- Interesting symbols: headers and holes
- Holes are often used for debug purposes on your board, but you also sometimes put them as mechanical holes for mounting, and you also sometimes put them as schematic placeholders for decorative elements of your PCB such as logos
- Basically MS paint - any symbol connects to any footprint as long as the number of pins matches

Assigning a footprint
- Tools -> Assign footprints
- Footprint filters at the top
- Footprint libraries on the left - so there's components sorted by group
- SMD -> surface mount parts vs THT -> through hole parts
- So in industry, SMD is common, and it's actually to solder from class
- Packages - ICs, integrated circuits live in them..
- BGA - ball grid array..
- SOT - popular for transistors...
- DIP - popular for op-amps for example...
- Connectors..  that's a whole category of things
- Some of them have company names in name
- Finding the right footprint?
- On Digikey - there's package/case category and you can look at the datasheet
- 0603, 0201.. etc capacitors, resistors, LEDs
    	- Metric vs. Imperial - common mistake!
- OK

Circuit board
- Always do schematic first
- Update PCB with changes made to schematic -> Update PCB
- Ratsnet
- The thing with undoing the ratsnet - first you move the components in place
- You want to minimize trace length
- Blue ratsnets will help you find closest connection
- Use R to rotate
- Add traces
- You also want to avoid right angles when making your traces
- Technically you can do rounded traces
- The default for boards is set up to be two-layers
- Front and back copper
- Allows you to do things that would otherwise intersect on a board
- Edge cuts - create physical, mechanical boundaries
- cool kids and professionals use arcs to add curved edges to the board
- Filled zone - huge pools of coppers
- common to do GND on both layers to minimize number of traces
- will not interfere with your existing traces, however, you might end up with small isolated islands of copper pools which you might need to join
- Design Rules Check aka DRC - like ERC but more important
- Refill all zones - will autogenerate pools within your boundaries set earlier
- Silkscreen
- White are just Kicad designators
- Yellow will actually show up on the board - that's the silkscreen
- You can add pictures and logos - silkscreen can be anything you want that your manufacturer allows and that your wallet is capable of funding
- Vias - are holes through your board
- Net - is essentially a node from KCL
- You can assign a net to a via
    	- net shows up on the Via
- This allows you to route traces from one layer to another
    	- Elevator, Elon Musk tunnels
- They also allow you to connect fill or pours from one side of the board to the other
- Mechanical holes are a type of footprint
- You can also technically add footprints without having symbols
- But that's bad practice
- And can create your own footprints
- At the end you run the DRC test and hope it passes
- You can add the settings for stuff like trace widths, and distanced between components and traces
- For BAC for example, they have specific rules that you can import into Kicad and then the DRC will tell you if your board is manufacturable

TA DA!!

New Board Ideassss
Add a gyroscope for better positioning and calibration
Add fans at the bottom for FUNSIES - I mean, for better speed and less friction uwu
Maybe switch one of the motor polarities?
Or it’s a good teaching tool and we should let them suffer 
Which I also support (Lucy’s not evil but Lucy do be on the evil spectrum)
Quality of life things - maybe 
Back LEDs - people usually burn them…
THT or SMD? Holding it in place, aligning them.. No stencils or holes etc.. 
Why if it’s on the back or front? Etc 
Switches? Usually they just short those 
Small in one dimension so they often short those 
Add a thermometer for funzies
So how do we make this accessible to people who have never heard of solder before? 
Maybe picking slightly larger parts? 
Maybe having two versions, one that’s less complex? The components would be annoying tho…
Or continue pre-soldering them
Any improvements we want to the wheeled drive?
Maybe add a third wheel or caster wheel? So it doesn’t drag?
Maybe a better motor mount that’s easier to print? Although it’s mostly just our 3d printing skills and screws, maybe test the screws and holes.. 

