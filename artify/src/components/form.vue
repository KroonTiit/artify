<template>
  <div>
    <p>Please enter your name and pick the Sectors you are currently involved in.</p>
    <label for="name">Name:</label>
    <input id="name" type="text"/>
    <label>Select Skills</label> 

    <multiselect v-model="selected"
      :options="options">
    </multiselect>
    <label for="terms">Agree to terms</label>
    <input id="terms" type="checkbox"/> 
    <input type="submit" value="Save"/>
  </div>
</template>

<script>
 import Multiselect from 'vue-multiselect'
  
export default {
  name: 'Form',
  props: {
    msg: String
  },
  components: { Multiselect },
    data () {
      return {
        selected: null,
        options: [   "Manufacturing",
      "Construction materials",
      "Electronics and Optics",
      "Food and Beverage",
      "Bakery & confectionery products",
      "Beverages",
      "Fish & fish products ",
      "Meat & meat products",
      "Milk & dairy products ",
      "Other",
      "Sweets & snack food",
      "Furniture",
      "Bathroom/sauna ",
      "Bedroom",
      "Children’s room ",
      "Kitchen ",
      "Living room ",
      "Office",
      "Other (Furniture)",
      "Outdoor ",
      "Project furniture",
      "Machinery",
      "Machinery components",
      "Machinery equipment/tools",
      "Manufacture of machinery ",
      "Maritime",
      "Aluminium and steel workboats ",
      "Boat/Yacht building",
      "Ship repair and conversion",
      "Metal structures",
      "Other",
      "Repair and maintenance service",
      "Metalworking",
      "Construction of metal structures",
      "Houses and buildings",
      "Metal products",
      "Metal works",
      "CNC-machining",
      "Forgings, Fasteners ",
      "Gas, Plasma, Laser cutting",
      "MIG, TIG, Aluminum welding",
      "Plastic and Rubber",
      "Packaging",
      "Plastic goods",
      "Plastic processing technology",
      "Blowing",
      "Moulding",
      "Plastics welding and processing",
      "Plastic profiles",
      "Printing ",
      "Advertising",
      "Book/Periodicals printing",
      "Labelling and packaging printing",
      "Textile and Clothing",
      "Clothing",
      "Textile",
      "Wood",
      "Other (Wood)",
      "Wooden building materials",
      "Wooden houses",
      "Other",
      "Creative industries",
      "Energy technology",
      "Environment",
      "Service",
      "Business services",
      "Engineering",
      "Information Technology and Telecommunications",
      "Data processing, Web portals, E-marketing",
      "Programming, Consultancy",
      "Software, Hardware",
      "Telecommunications",
      "Tourism",
      "Translation services",
      "Transport and Logistics",
      "Air",
      "Rail",
      "Road",
      "Water"]
      }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="../styles/main.less" lang="less" scoped></style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
