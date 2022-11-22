# Perfection Pet Foods Project
## Summary
Perfection Pet Foods (PPF), a co-manufacturer serving the pet food industry, seeks to optimize their management of empty bag inventory. They need us to develop an inventory control policy that will minimize cost.
##  About Perfection Pet Foods
Perfection Pet Foods’ extensive production and manufacturing capabilities are what set them apart from the competition. From super premium, non-grain pet food to mass consumer private label products, they consistently deliver the highest quality product to both retailers and consumers. Their plant in Visalia, CA is a state-of-the-art dry kibble production facility, bringing much needed co-pack capacity and capability to the west coast. The plan typically operates on a 24/7 basis, with down days planned accordingly for preventative maintenance and to manage supply/demand balance.

## Keywords and concepts   
- Kibble: another word for the food itself.
- A packaged bag of pet food is referred to as a finished good (FG) product.
- Mono-kibble product: a FG product that consists of a single kibble.
- Multi-kibble: a FG product that consists of a mixture of two or more kibbles.
- Component formula: a single type of kibble
- Master formula: the contents of a FG product that goes in a bag. A master formula may consist of a single
component formula (mono-kibble) or multiple component formulas (multi-kibble). 
## Process Description
At PPF, pet food is manufactured in two stages: extrusion and pack out.
- Extrusion. First, the pet food is extruded, taking in batched ingredients, through extruding machines which create
the actual kibble. The plant has three extruders, and the extrusion rate is given in the data spreadsheet. (Following extrusion, product goes through ovens to dry to desired moisture, but this process may be ignored for this assignment.) It is possible for an extruder two switch bins during a production run.
- Pack out. After the kibble is extruded, it is packaged into (sellable) bags, which may be mono-kibble or multikibble. There are four pack lines: one for small bags (called the Parsons line) and three for medium and large bags (called Umbra, Premier Tech, and Thiele, respectively). The throughput rate for the packing process depending on the pack line as well as the kibble type. The pack lines can start pulling kibble before a bin is full. There is no room on the pack lines for staging kibble.
## Objective
Develop an inventory policy that minimizes amount spent on bags while covering all forecasted production needs (including potential variability) and not exceeding space constraints on site or at supplier.
## Data
• “Item Mapping and Pricing” tab
o Detail of Finished good items and associated Bag ID’s.
o Unit Weights of each item.
o Lead time in weeks per item.
o Cost per bag: each column represents the cost per bag if purchasing up to a certain amount. For example, the
“10M” column gives the price per bag if the order quantity 10,000 bags or more and the “15M” gives the price per bag if the quantity is more than 15,000 up to the next provided price/qty. If a cell is blank for a particular row, then the price per bag is taken to be the closest non-empty value from the left. For example, for BAG ID B1012, the price per bag when ordering up to 10,000 bags is $1.00 and the price for ordering more than 10,000 but no more than 20,000 is $0.86.
o Minimum order quantity (MOQ): The first price point provided for each bag type is the MOQ for that type. So for B1015, the MOQ is 25,000.
• “Item Demand” tab
 This represents the forecasted production needs in lbs for each week.
## Other information
• Yield loss
o You should assume a 10% yield loss on bags when running. So, if the run is 200,000# of 40# Bags, bag
needs are 200,000/40 = 5,000 bags / (1 – 0.1) = 5,556 bags. • V ariability
    o You should assume that actual bag needs could vary +/- 15% from forecasted need. Thus, you should make sure that the inventory level each product in each week does not drop below 0.15 times the demand for that week.
• Inventory Space Constraints
o Total weeks-of-supply (WOS) space on site is 7 WOS. This is a total across all items. Slow moving
items may be 13+ WOS, fast moving may be 2 WOS, but overall should be capped at 7 WOS.
• Additionally, the supplier can hold up to 7 WOS of empty bags at no charge, then release in minimal order
quantity (MOQ) amounts as needed. It is important to note that the supplier views this as no more than 7 weeks storage for each item, not in aggregate. When any item has been sitting for 7 weeks, the supplier will auto ship to PFF and the item will be received in one week. This capability should help minimize on site FG inventory, and also help maximize order increments to take advantage of lower prices with higher order amounts.
§ For example, we can order 100,000 bags, bring in 20,000 and keep 80,000 at supplier. Then release in increments of 20,000 until remaining 80,000 are consumed.