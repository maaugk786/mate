import re
import streamlit as st
import streamlit.components.v1 as components

# Set up the Streamlit page
st.set_page_config(page_title="Materials Engineering", layout="wide")

raw_data = """Section 1: Material Structure & Characterization (Lecture 10)
Which level of structure can be observed with the naked eye?
A) Microstructure B) Macrostructure C) Nanostructure D) Mesostructure
Answer: B
Which structure size is on the borderline of visibility?
A) Nanostructure B) Macrostructure C) Mesostructure D) Microstructure
Answer: C
What is the typical size of objects viewed in a microstructure using optical microscopy?
A) ~1 mm B) ~0.001 mm C) ~1 nm D) ~100 nm
Answer: B
What is the size range for nanostructures?
A) 1-100 nm B) 1-100 mm C) 100-1000 nm D) 0.001-0.1 mm
Answer: A
Which characterization method uses visible light?
A) XRD B) SEM C) Optical Microscopy D) TEM
Answer: C
Which of the following uses X-rays for characterization?
A) XRD and XPS B) SEM and TEM C) SIMS and FIB D) AES and EELS
Answer: A
Which characterization method uses neutrons?
A) ND B) EDS C) WDS D) OM
Answer: A
Which method uses ion beams, often for cleaning and thinning samples?
A) XPS B) FIB C) XRD D) TEM
Answer: B
Which of the following is NOT an electron beam characterization method?
A) SEM B) TEM C) SIMS D) EDS
Answer: C
What does the "response to external stimulus" define in materials science?
A) Processing B) Structure C) Material Characteristic D) Performance
Answer: C
What is the primary purpose of Non-Destructive Testing (NDT)?
A) To test materials until they break B) To evaluate properties without causing damage C) To alter the material's microstructure D) To melt and recast materials
Answer: B
Which of the following is an advantage of NDT?
A) Destroys the sample for accurate reading B) Cost-effectiveness C) Requires high temperatures D) Changes mechanical properties
Answer: B
How does NDT improve safety?
A) By hardening the material B) By providing early warning of potential issues C) By making the material heavier D) By increasing the material's yield strength
Answer: B
Which NDT method uses capillary action?
A) Ultrasonic Testing B) Radiography C) Liquid Penetrant Testing D) Magnetic Particle Testing
Answer: C
Liquid Penetrant Testing is strictly limited to detecting:
A) Deep internal voids B) Surface-breaking defects C) Variations in density D) Magnetic anomalies
Answer: B
What is the first step in Liquid Penetrant Inspection?
A) Apply developer B) Apply penetrant C) Clean the surface D) Inspect under UV light
Answer: C
What is the purpose of the "developer" in liquid penetrant testing?
A) To harden the surface B) To draw the penetrant out of the flaw C) To magnetize the part D) To dissolve the penetrant
Answer: B
Magnetic Particle Testing is only applicable to which type of materials?
A) Polymers B) Ceramics C) Ferromagnetic materials D) Non-ferrous alloys
Answer: C
In Magnetic Particle Testing, what causes the magnetic particles to cluster?
A) Capillary action B) Magnetic flux leakage C) High-frequency sound waves D) Eddy currents
Answer: B
Magnetic Particle Testing can detect flaws located where?
A) At the surface and slightly subsurface B) Deep in the core only C) Only on the surface D) Only in non-metals
Answer: A
What type of waves does Ultrasonic Testing use?
A) X-rays B) Low-frequency light C) High-frequency sound waves D) Gamma rays
Answer: C
In Ultrasonic Testing, what happens when sound waves hit a boundary or flaw?
A) They accelerate B) They are absorbed completely C) They are reflected back to the receiver D) They change into light waves
Answer: C
Which NDT method is commonly used to measure material thickness?
A) Liquid Penetrant B) Magnetic Particle C) Ultrasonic Testing D) Visual Inspection
Answer: C
Eddy current inspection utilizes which type of currents?
A) Direct currents (DC) B) Alternating currents (AC) C) Static electricity D) Acoustic waves
Answer: B
Eddy current flow patterns are disturbed by:
A) Changes in color B) Presence of cracks or discontinuities C) Variations in light intensity D) The surrounding air pressure
Answer: B
Eddy current testing is typically performed on:
A) Plastics B) Metallic sections C) Wood D) Glass
Answer: B
Radiographic testing uses which types of radiation?
A) Alpha and Beta rays B) Visible light and Infrared C) X-rays and Gamma rays D) Microwaves and Radio waves
Answer: C
In radiography, more radiation passes through areas with:
A) Higher thickness B) Higher density C) Lower thickness or lower density (e.g., a void) D) Magnetic fields
Answer: C
How does a crack appear on a traditional radiographic film?
A) Lighter than the surrounding area B) Darker than the surrounding area C) The same color as the surrounding area D) It does not appear
Answer: B
Digital radiography uses what instead of traditional film?
A) Photographic paper B) X-ray image intensifiers or radioscopy systems C) Magnetic tape D) Liquid penetrant
Answer: B
Section 2: Destructive Testing & Mechanical Properties (Lecture 11)
Mechanical properties refer to a material's behavior under:
A) Thermal heating B) External forces C) Chemical reactions D) Light exposure
Answer: B
What occurs when a material undergoes elastic deformation?
A) Planes shear permanently B) Bonds stretch but return to initial state upon unloading C) The material fractures D) The material melts
Answer: B
Elastic deformation is:
A) Permanent B) Reversible C) Non-linear in all metals D) A form of fracture
Answer: B
Which material typically exhibits non-linear elastic behavior?
A) Mild steel B) Aluminum C) Grey iron and polymers D) Copper
Answer: C
What causes plastic deformation at the atomic level in metals?
A) Bond stretching only B) Bonds stretch and planes shear C) Evaporation of surface atoms D) Magnetic domain alignment
Answer: B
Plastic deformation is defined as:
A) Reversible B) Temporary C) Permanent D) Non-existent in metals
Answer: C
Engineering stress is defined as:
A) Load divided by instantaneous area B) Load divided by original cross-sectional area C) Change in length divided by original length D) Original length divided by load
Answer: B
What is the formula for engineering strain?
A) e = P/Ao B) e = ΔL/Lo C) e = Lo/ΔL D) e = Ao/P
Answer: B
The transition from elastic to plastic deformation is known as:
A) Fracture B) Yielding C) Necking D) Creep
Answer: B
For most metals, the yield strength is determined using a strain offset of:
A) 0.002 B) 0.02 C) 0.2 D) 2.0
Answer: A
What is the Tensile Strength (TS) on a stress-strain curve?
A) The lowest stress point B) The point of fracture C) The maximum stress D) The point of elastic limit
Answer: C
What happens to a metal immediately after reaching its Tensile Strength?
A) It returns to its original shape B) Necking begins C) It becomes stronger D) It enters the linear elastic region
Answer: B
Which property measures a material's ability to deform plastically without fracturing?
A) Brittleness B) Ductility C) Stiffness D) Resilience
Answer: B
Ductility is commonly quantified by:
A) Yield strength B) Tensile strength C) Percent Elongation (%EL) or Percent Reduction in Area (%RA) D) Hardness
Answer: C
A highly ductile material will have a:
A) Large %EL B) Low %EL C) Zero %EL D) Negative %EL
Answer: A
What is resilience?
A) Energy absorbed before fracture B) Energy absorbed during elastic deformation C) Resistance to localized deformation D) Resistance to cyclic loading
Answer: B
How is the modulus of resilience represented graphically?
A) Area under the entire stress-strain curve B) The slope of the elastic region C) Area under the elastic region of the stress-strain curve D) The maximum height of the curve
Answer: C
What is toughness?
A) Resistance to scratching B) Ability to absorb energy up to fracture C) Ability to stretch elastically D) Time-dependent deformation
Answer: B
Toughness is represented graphically as:
A) The peak of the stress-strain curve B) Area under the elastic region C) Area under the entire stress-strain curve D) The strain at fracture
Answer: C
Hardness is a measure of a material's resistance to:
A) General elastic deformation B) Localized plastic deformation C) Thermal expansion D) Fatigue failure
Answer: B
Which hardness test uses a 10 mm sphere of steel or tungsten carbide?
A) Vickers B) Knoop C) Brinell D) Rockwell
Answer: C
In the Brinell hardness test, the hardness number is a function of:
A) The depth of the indentation B) The load and the diameter of the resulting indentation C) The time the load is applied D) The rebound height
Answer: B
Which hardness test measures the difference in depth of penetration between a minor and major load?
A) Brinell B) Vickers C) Rockwell D) Knoop
Answer: C
The Vickers hardness test uses what type of indenter?
A) A steel sphere B) A diamond cone C) A diamond pyramid D) A tungsten carbide sphere
Answer: C
Which two tests are considered microindentation hardness tests?
A) Brinell and Rockwell B) Vickers and Knoop C) Rockwell and Vickers D) Brinell and Knoop
Answer: B
The Knoop hardness test is particularly useful for testing:
A) Large steel beams B) Very brittle materials or thin layers C) Liquid metals D) Rubber
Answer: B
True stress is based on:
A) Original cross-sectional area B) Instantaneous cross-sectional area C) Original length D) Instantaneous length
Answer: B
Why does the engineering stress curve drop after the tensile strength is reached?
A) The material actually gets weaker B) The cross-sectional area decreases rapidly due to necking C) The material cools down D) The bonds stiffen
Answer: B
What happens to Yield Strength and Tensile Strength as a metal is plastically deformed (strain hardened)?
A) They decrease B) They remain constant C) They increase D) They drop to zero
Answer: C
What happens to ductility as a metal is strain hardened?
A) It increases B) It decreases C) It stays the same D) It fluctuates
Answer: B
Fatigue failure occurs under what type of loading?
A) Constant static loading B) Dynamic and fluctuating (cyclic) loading C) Sudden high-temperature spikes D) Zero loading
Answer: B
Fatigue can cause failure at stress levels:
A) Considerably higher than the yield strength B) Only at the ultimate tensile strength C) Considerably lower than the tensile or yield strength D) Only at absolute zero
Answer: C
Which test is used to measure fatigue properties?
A) Tensile test B) Brinell test C) Rotating-bending test D) Impact test
Answer: C
What does an S-N curve plot?
A) Stress vs. Strain B) Stress amplitude vs. Number of cycles to failure C) Strength vs. Necking D) Strain vs. Number of indentations
Answer: B
What is the "fatigue limit" (or endurance limit)?
A) The maximum stress before yielding B) The stress level below which fatigue failure will not occur C) The number of cycles it takes to fail at maximum stress D) The temperature at which fatigue begins
Answer: B
What type of materials typically display a distinct fatigue limit?
A) Nonferrous alloys B) Many steels and titanium alloys C) Polymers D) Ceramics
Answer: B
If a material does not have a distinct fatigue limit, what property is specified instead?
A) Fatigue strength at a specific number of cycles B) Yield point C) Creep rate D) Ultimate tensile strength
Answer: A
What is creep?
A) Rapid failure under impact B) Time-dependent permanent deformation under constant load or stress C) Localized surface scratching D) Reversible stretching
Answer: B
Creep is usually only significant when the temperature is:
A) Below 0°C B) Above the melting point C) Greater than 0.4 Tm (absolute melting temperature) D) Exactly at room temperature
Answer: C
The slope of the secondary (steady-state) region on a creep curve is called the:
A) Yield point B) Creep rate C) Rupture lifetime D) Elastic modulus
Answer: B
What happens to the steady-state creep rate as temperature or stress increases?
A) It decreases B) It remains constant C) It increases D) It drops to zero
Answer: C
What happens to the rupture lifetime as temperature or stress increases?
A) It increases B) It decreases C) It remains constant D) It becomes infinite
Answer: B
The primary region of a creep curve exhibits:
A) Increasing creep rate B) Constant creep rate C) Decreasing creep rate D) Instantaneous fracture
Answer: C
The tertiary region of a creep curve exhibits:
A) Decreasing creep rate B) Acceleration of creep rate leading to rupture C) A flat, constant slope D) Elastic recovery
Answer: B
Destructive testing is mainly used to:
A) Inspect components in active service B) Determine fundamental mechanical properties of materials C) Clean the surface of metals D) Check for surface cracks without damaging the part
Answer: B
In an S-N curve, the 'S' stands for:
A) Strain B) Stress Amplitude C) Shear D) Stiffness
Answer: B
An alloy with larger grains will generally have what effect on creep resistance?
A) Decreased resistance B) Increased resistance C) No effect D) Causes immediate rupture
Answer: B
The capability of a material to withstand a sudden blow is measured by:
A) Fatigue testing B) Creep testing C) Impact testing D) Hardness testing
Answer: C
The Charpy and Izod tests are examples of:
A) Hardness tests B) Fatigue tests C) Impact tests D) Creep tests
Answer: C
A material that fails with very little plastic deformation is considered:
A) Ductile B) Tough C) Brittle D) Resilient
Answer: C
Section 3: Classification & Properties of Metallic Alloys (Lecture 14)
Metallic alloys are broadly classified into which two categories?
A) Polymers and Ceramics B) Ferrous and Nonferrous C) Composites and Metals D) Natural and Synthetic
Answer: B
Ferrous metals are defined as metals containing a high percentage of:
A) Aluminum B) Copper C) Iron D) Titanium
Answer: C
Which of the following is NOT a ferrous metal?
A) Carbon Steel B) Cast Iron C) Aluminum D) Stainless Steel
Answer: C
Nonferrous metals do not contain significant amounts of:
A) Carbon B) Zinc C) Iron D) Magnesium
Answer: C
Which of the following is a nonferrous metal?
A) Alloy steel B) Pig iron C) Copper D) Tool steel
Answer: C
Steels are primarily an alloy of iron and:
A) Zinc B) Copper C) Carbon D) Nickel
Answer: C
Low carbon steel generally contains what percentage of carbon?
A) Less than 0.25% B) 0.25% to 0.60% C) 0.60% to 1.4% D) 2.14% to 4.5%
Answer: A
Medium carbon steels generally contain what percentage of carbon?
A) <0.25% B) 0.25% to 0.60% C) 0.60% to 1.4% D) >2.14%
Answer: B
High carbon steels generally contain what percentage of carbon?
A) 0.05% to 0.15% B) 0.25% to 0.60% C) 0.60% to 1.4% D) >4.0%
Answer: C
Cast irons typically contain carbon in the range of:
A) 0.1% to 0.5% B) 0.6% to 1.0% C) 2.14% to 4.5% D) 10% to 20%
Answer: C
Which of the following is a type of cast iron?
A) Stainless B) High-strength low-alloy C) Grey D) Galvanized
Answer: C
The property of a material to regain its original shape after load removal is:
A) Plasticity B) Elasticity C) Brittleness D) Malleability
Answer: B
The limit up to which a material can regain its original shape is the:
A) Plastic limit B) Ultimate limit C) Elastic limit D) Fracture point
Answer: C
The property by which a material is permanently deformed without rupture is:
A) Elasticity B) Plasticity C) Stiffness D) Resilience
Answer: B
The ability of a material to resist deformation due to external forces is called:
A) Ductility B) Brittleness C) Stiffness D) Malleability
Answer: C
The property of a material to break easily into pieces without deformation is:
A) Ductility B) Malleability C) Brittleness D) Toughness
Answer: C
Glass and cast iron are typically examples of materials that are:
A) Highly ductile B) Malleable C) Brittle D) Elastic
Answer: C
The ability of a material to be drawn into wires is called:
A) Malleability B) Ductility C) Brittleness D) Stiffness
Answer: B
The ability of a material to be rolled or hammered into thin sheets is called:
A) Ductility B) Malleability C) Stiffness D) Resilience
Answer: B
Adding chromium to steel primarily improves its:
A) Density B) Corrosion resistance C) Electrical conductivity D) Brittleness
Answer: B
Which alloying element is added to steel to make stainless steel?
A) Lead B) Chromium C) Zinc D) Tin
Answer: B
What effect does increasing carbon content have on steel?
A) Increases ductility B) Decreases strength C) Increases hardness and strength D) Increases malleability
Answer: C
Which category of metal fabrication involves shaping a solid metal piece using force?
A) Casting B) Forming C) Joining D) Welding
Answer: B
Forging, rolling, and extrusion are examples of:
A) Joining B) Casting C) Forming D) Heat treatment
Answer: C
What is the process of pouring molten metal into a mold to cool and solidify?
A) Forging B) Extrusion C) Casting D) Welding
Answer: C
Which casting method is typically used for large parts like auto engine blocks?
A) Investment Casting B) Sand Casting C) Continuous Casting D) Die Casting
Answer: B
Which casting method uses a wax pattern encased in plaster?
A) Sand Casting B) Die Casting C) Investment Casting D) Continuous Casting
Answer: C
Investment casting is well-suited for:
A) High volume, simple shapes B) Low volume, complex shapes (e.g., jewelry) C) Continuous slabs D) Large iron pipes
Answer: B
Which casting method forces molten metal into a mold under high pressure?
A) Sand Casting B) Die Casting C) Investment Casting D) Continuous Casting
Answer: B
Die casting is generally used for:
A) High volume, low melting temperature alloys B) Low volume, high temperature alloys C) Large steel blocks D) Complex wax shapes
Answer: A
Which casting method produces simple slab shapes in an uninterrupted process?
A) Sand Casting B) Continuous Casting C) Investment Casting D) Die Casting
Answer: B
Powder metallurgy is typically used for materials that have:
A) Low melting points B) High ductility C) Low ductility D) High transparency
Answer: C
Powder metallurgy involves applying pressure and heat to powder, a process known as:
A) Casting B) Forging C) Sintering / Densification D) Extrusion
Answer: C
Welding is classified under which type of metal fabrication?
A) Forming B) Casting C) Joining D) Sintering
Answer: C
What is the Heat Affected Zone (HAZ) in welding?
A) The area where the metal remains completely unchanged B) The region where the microstructure is changed by heat C) The filler metal before it melts D) The cooling tank
Answer: B
In welding, what is used to bridge the gap between piece 1 and piece 2?
A) Wax prototype B) Plaster mold C) Filler metal D) Sand
Answer: C
Which property must be low for a material to be processed easily via powder metallurgy?
A) Hardness B) Melting point C) Ductility D) Brittleness
Answer: C
What is the primary difference between forming and casting?
A) Casting uses solid metal; forming uses molten metal B) Casting uses molten metal; forming reshapes solid metal C) Casting only joins parts together D) Forming cannot be used on metals
Answer: B
Drawing is a forming process used to make:
A) Sheets B) Blocks C) Wires D) Powders
Answer: C
Rolling is a forming process primarily used to produce:
A) Complex jewelry B) Wires C) Sheets or plates D) Hollow tubes
Answer: C
The property of stiffness is directly related to which mechanical modulus?
A) Modulus of Toughness B) Modulus of Elasticity C) Modulus of Rupture D) Bulk Modulus
Answer: B
A metal that is easily shaped by hammering without cracking is highly:
A) Brittle B) Malleable C) Elastic D) Stiff
Answer: B
High strength low alloy (HSLA) steels are a subcategory of:
A) High carbon steels B) Low carbon steels C) Cast irons D) Nonferrous alloys
Answer: B
Tool steels fall under which category?
A) Low carbon steels B) Medium carbon steels C) High carbon steels D) Cast irons
Answer: C
White cast iron is known for being extremely:
A) Soft and ductile B) Hard and brittle C) Elastic and resilient D) Malleable
Answer: B
Ductile cast iron is created by adding which element to the melt?
A) Chromium B) Magnesium or Cerium C) Zinc D) Lead
Answer: B
Which cast iron has graphite in the form of flakes?
A) White cast iron B) Malleable cast iron C) Grey cast iron D) Ductile cast iron
Answer: C
Why is grey cast iron weak and brittle in tension?
A) It lacks carbon B) The graphite flakes act as stress concentrators C) It contains too much magnesium D) It has a purely austenitic structure
Answer: B
Malleable iron is produced by heat treating which type of iron?
A) Grey iron B) Ductile iron C) White iron D) Wrought iron
Answer: C
Which metal fabrication method is preferred when one single large part is impractical to cast or form?
A) Forging B) Extrusion C) Joining (Welding) D) Powder metallurgy
Answer: C
The "yield point" on a stress-strain curve indicates the end of:
A) Plasticity B) Necking C) Elastic behavior D) Fracture
Answer: C
Stress is calculated by dividing force by:
A) Volume B) Density C) Length D) Area
Answer: D
Strain is a measure of:
A) Force applied B) Heat absorbed C) Deformation (change in length relative to original length) D) Time to failure
Answer: C
Which test involves pulling a sample apart until it breaks?
A) Hardness test B) Tensile test C) Impact test D) Fatigue test
Answer: B
What defines the linear region of a stress-strain curve?
A) Hooke's Law B) Newton's Law C) Ohm's Law D) Pascal's Law
Answer: A
The area under the entire stress-strain curve up to fracture represents:
A) Elasticity B) Resilience C) Toughness D) Hardness
Answer: C
Which of the following defines resilience?
A) Capacity to absorb energy in the plastic range B) Capacity to absorb energy in the elastic range C) Resistance to scratching D) Resistance to cyclic loads
Answer: B
Creep is a concern primarily at:
A) Cryogenic temperatures B) Room temperature C) High temperatures D) In a vacuum
Answer: C
The number of cycles a material can endure at a specific stress amplitude is the:
A) Creep life B) Fatigue life C) Yield limit D) Tensile strength
Answer: B
Which of these tests does NOT measure hardness?
A) Rockwell B) Brinell C) Charpy D) Vickers
Answer: C
The Rockwell test utilizes varying:
A) Indenter shapes and applied loads (minor and major) B) Sound wave frequencies C) Acid solutions D) Electric currents
Answer: A
A material with high hardness will generally have:
A) High ductility B) High wear resistance C) Low stiffness D) High plasticity
Answer: B
Which technique is used to observe grains and grain boundaries?
A) Naked eye observation B) Optical Microscopy C) Ultrasonic testing D) Liquid penetrant
Answer: B
Which NDT method is best for detecting subsurface flaws in a steel bar?
A) Visual Inspection B) Liquid Penetrant C) Ultrasonic Testing D) Naked eye
Answer: C
X-Ray Diffraction (XRD) primarily helps determine:
A) Surface cracks B) Crystal structure and phases C) Ultimate tensile strength D) Magnetic domains
Answer: B
Which destructive test measures the energy required to break a notched specimen?
A) Tensile B) Hardness C) Impact (Charpy/Izod) D) Fatigue
Answer: C
A large area under the stress-strain curve indicates the material is:
A) Brittle B) Tough C) Soft D) Weak
Answer: B
A steep slope in the linear elastic region indicates a high:
A) Ductility B) Modulus of Elasticity (Stiffness) C) Creep rate D) Fatigue limit
Answer: B
"Necking" occurs in which region of the stress-strain curve?
A) Linear elastic region B) Between yield point and tensile strength C) After the ultimate tensile strength D) During elastic unloading
Answer: C
True strain is defined using the:
A) Original length B) Instantaneous length C) Original area D) Fracture area
Answer: B
Which factor decreases a metal's ductility?
A) Heating it to melting point B) Strain hardening (cold working) C) Annealing D) Polishing
Answer: B
Fatigue failure is dangerous because it often occurs:
A) Without visible warning or macroscopic plastic deformation B) Only at temperatures above melting point C) Only when the metal is stretched to 200% its length D) During the elastic phase of a single pull
Answer: A
What is the typical failure mode for brittle materials?
A) Extensive necking B) Sudden catastrophic fracture C) Gradual creep D) High percent elongation
Answer: B
Cast irons are preferred for applications requiring:
A) High tension stretching B) Drawing into fine wires C) Good castability and wear resistance D) Extreme lightness
Answer: C
Why is aluminum widely used in aerospace?
A) High density B) Ferromagnetic properties C) High strength-to-weight ratio D) High carbon content
Answer: C
Steel is fundamentally an alloy of iron and:
A) Oxygen B) Carbon C) Nitrogen D) Helium
Answer: B
Increasing the carbon content in steel increases its:
A) Malleability B) Ductility C) Strength and hardness D) Corrosion
Answer: C
Stainless steel is resistant to corrosion primarily due to the addition of:
A) Carbon B) Chromium C) Lead D) Tungsten
Answer: B
Which manufacturing process involves pushing metal through a die to create long continuous shapes?
A) Forging B) Extrusion C) Sand casting D) Welding
Answer: B
Which process is considered "Joining"?
A) Rolling B) Welding C) Extrusion D) Die casting
Answer: B
Investment casting is also known as:
A) Sand casting B) Lost-wax casting C) Continuous casting D) Die casting
Answer: B
Powder metallurgy relies on atomic diffusion at high temperatures, a process called:
A) Sintering B) Melting C) Forging D) Extrusion
Answer: A
The region of base metal altered by the heat of welding is the:
A) Fusion zone B) Heat Affected Zone (HAZ) C) Cold worked zone D) Sintered zone
Answer: B
What happens to the mechanical properties in the HAZ?
A) They remain identical to the base metal B) They are often altered or degraded C) They always improve dramatically D) The metal turns into a polymer
Answer: B
The property related to wire drawing is:
A) Brittleness B) Stiffness C) Ductility D) Hardness
Answer: C
The property related to rolling metal into sheets is:
A) Malleability B) Ductility C) Brittleness D) Elasticity
Answer: A
Which of the following represents a dynamic load test?
A) Brinell hardness B) Fatigue test C) Creep test D) Static tensile test
Answer: B
Which test measures behavior at elevated temperatures over long periods?
A) Charpy impact B) Creep test C) Tensile test D) Vickers test
Answer: B
What is required to initiate plastic deformation?
A) Stress must exceed the yield strength B) Stress must equal zero C) Stress must be below the elastic limit D) Temperature must be at absolute zero
Answer: A
Which equation represents Hooke's Law (where E is Modulus of Elasticity, σ is stress, ε is strain)?
A) σ = E / ε B) σ = E * ε C) ε = σ * E D) E = σ * ε
Answer: B
If a material absorbs little energy before it breaks, it is:
A) Tough B) Ductile C) Brittle D) Malleable
Answer: C
Hardness tests are often preferred over tensile tests because they are:
A) Slower B) More destructive C) Less destructive and quicker D) Require melting the sample
Answer: C
The Knoop test is a type of:
A) Impact test B) Microindentation hardness test C) Creep test D) Fatigue test
Answer: B
Which of the following is NOT an advantage of Non-Destructive Testing?
A) Lowers cost by preventing breakdown B) Modifies the material to be stronger C) Improves safety D) Maintains the integrity of the part
Answer: B
Dye penetrant inspection relies on a liquid's ability to enter a crack via:
A) Magnetic attraction B) Gravity C) Capillary action D) High pressure
Answer: C
To use magnetic particle inspection, the material must be:
A) Transparent B) Non-metallic C) Ferromagnetic D) A liquid
Answer: C
Ultrasonic testing detects flaws by measuring:
A) Electrical resistance B) Reflected sound waves C) Magnetic leakage D) Radiation absorption
Answer: B
Eddy current testing relies on the material's:
A) Electrical conductivity B) Density C) Color D) Melting point
Answer: A
Radiography detects internal flaws because a void will:
A) Block X-rays completely B) Absorb more radiation than the solid metal C) Allow more radiation to pass through than the solid metal D) Reflect the X-rays back
Answer: C
Microstructure requires what to be seen?
A) Naked eye B) Optical microscopy C) X-ray diffraction only D) Only a ruler
Answer: B
Transmission Electron Microscopy (TEM) utilizes a beam of:
A) Protons B) Neutrons C) Electrons D) Photons
Answer: C
Which property is the "ability to withstand applied forces without breaking"?
A) Thermal conductivity B) Mechanical strength C) Optical transparency D) Density
Answer: B
Strain hardening is the result of:
A) Heating the metal B) Plastically deforming the metal C) Exposing the metal to magnetic fields D) Applying liquid penetrant
Answer: B
The fatigue limit is seen on a graph plotting:
A) Stress vs Strain B) Stress vs Cycles (S-N curve) C) Load vs Extension D) Strain vs Time
Answer: B
Creep rate is determined during which stage of the creep curve?
A) Primary (transient) B) Secondary (steady-state) C) Tertiary D) Instantaneous initial deformation
Answer: B
Which phase of the creep curve ends in rupture?
A) Primary B) Secondary C) Tertiary D) Elastic
Answer: C
Which test is used to measure fracture energy under rapid loading?
A) Tensile Test B) Charpy Impact Test C) Brinell Hardness D) Creep Test
Answer: B
In terms of percentage carbon, cast irons have:
A) Less carbon than low carbon steel B) Less carbon than high carbon steel C) More carbon than high carbon steel D) Zero carbon
Answer: C
Continuous casting is advantageous because it:
A) Makes highly complex jewelry B) Eliminates the need for multiple intermediate heating/rolling steps for simple shapes C) Uses plaster of Paris molds D) Is only used for low-melting alloys
Answer: B
What defines a 'ferrous' alloy?
A) It contains no iron B) It is made primarily of aluminum C) Iron is the base element D) It is a polymer
Answer: C
Yield strength is critical in engineering design because it marks the point where:
A) The material breaks B) Permanent structural deformation begins C) The material is perfectly elastic D) The test ends
Answer: B
Which non-destructive method is simplest and requires no special equipment?
A) Radiography B) Ultrasonic C) Visual Inspection D) Eddy Current
Answer: C
Magnetic Particle Inspection will NOT work on:
A) Low carbon steel B) Cast iron C) Aluminum D) High carbon steel
Answer: C
A disadvantage of Liquid Penetrant Testing is:
A) It only detects surface flaws B) It works on all materials C) It requires an X-ray source D) It is highly radioactive
Answer: A
Which variable is NOT essential to the creep process?
A) Constant stress/load B) Elevated temperature C) Time D) A magnetic field
Answer: D
Which process joins two pieces by melting the base metal and adding a filler metal?
A) Forging B) Extrusion C) Welding D) Die Casting
Answer: C
Which structural hierarchy is between 1 nm and 100 nm?
A) Macrostructure B) Mesostructure C) Microstructure D) Nanostructure
Answer: D
The "reduction in area" is a measure of a material's:
A) Elasticity B) Brittleness C) Ductility D) Hardness
Answer: C
High carbon steel is generally:
A) Softer than low carbon steel B) Harder and stronger than low carbon steel C) More ductile than low carbon steel D) Easier to weld than low carbon steel
Answer: B
What is a primary reason for using powder metallurgy?
A) To make large engine blocks B) To work with materials that have very low ductility C) To cast low melting point metals D) To perform visual NDT
Answer: B"""

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Materials Engineering Study Sheet</title>
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            line-height: 1.6; 
            max-width: 900px; 
            margin: 0 auto; 
            padding: 30px 20px; 
            background-color: #f8f9fa; 
            color: #212529; 
        }
        h1 { 
            text-align: center; 
            color: #1a237e; 
            border-bottom: 3px solid #3f51b5; 
            padding-bottom: 15px; 
            margin-bottom: 40px;
        }
        .section-title { 
            font-size: 1.4em; 
            color: #e65100; 
            margin-top: 40px; 
            margin-bottom: 20px;
            border-bottom: 2px solid #ffcc80; 
            padding-bottom: 8px;
            font-weight: bold;
        }
        .question-block { 
            background: #ffffff; 
            padding: 20px 25px; 
            margin-bottom: 20px; 
            border-radius: 8px; 
            box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
            border-left: 5px solid #3f51b5; 
        }
        .statement { 
            font-weight: 600; 
            font-size: 1.1em; 
            color: #1a237e; 
            margin-bottom: 12px;
        }
        .options { 
            color: #555; 
            margin-bottom: 12px;
            padding-left: 10px;
            border-left: 2px solid #e0e0e0;
        }
        .answer { 
            color: #2e7d32; 
            font-weight: 600; 
            background-color: #e8f5e9;
            padding: 10px 15px;
            border-radius: 5px;
            display: inline-block;
        }
        .label {
            font-weight: bold;
            color: #424242;
        }
    </style>
</head>
<body>
    <h1>Materials Engineering Study Sheet</h1>
"""

lines = raw_data.strip().split('\n')
i = 0
while i < len(lines):
    line = lines[i].strip()
    if not line:
        i += 1
        continue
        
    if line.startswith("Section"):
        html_content += f'<div class="section-title">{line}</div>\n'
        i += 1
        continue
        
    if "?" in line or not line.startswith("A)"): 
        question = line
        i += 1
        if i < len(lines):
            options_line = lines[i].strip()
            i += 1
            if i < len(lines):
                answer_line = lines[i].strip()
                i += 1
                
                if answer_line.startswith("Answer:"):
                    ans_letter = answer_line.split(":")[1].strip()
                    
                    match = re.search(r'A\)(.*?)B\)(.*?)C\)(.*?)D\)(.*)', options_line)
                    ans_text = ""
                    
                    if match:
                        opt_a, opt_b, opt_c, opt_d = [x.strip() for x in match.groups()]
                        if ans_letter == "A": ans_text = opt_a
                        elif ans_letter == "B": ans_text = opt_b
                        elif ans_letter == "C": ans_text = opt_c
                        elif ans_letter == "D": ans_text = opt_d
                    else:
                        ans_text = f"Option {ans_letter}"

                    html_content += f'''
                    <div class="question-block">
                        <div class="statement"><span class="label">Statement:</span> {question}</div>
                        <div class="options"><span class="label">Options:</span> {options_line}</div>
                        <div class="answer"><span class="label">Correct Answer:</span> {ans_text}</div>
                    </div>
                    '''

html_content += "</body></html>"

# This uses Streamlit's component to render the HTML visually on the app
components.html(html_content, height=800, scrolling=True)
