<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-12">
              <v-toolbar
                color="primary"
                dark
                flat
              >
                <v-toolbar-title>Skills form</v-toolbar-title>
                <v-spacer />
              </v-toolbar>
               <v-form 
                ref="form"
                v-model="valid"
                :lazy-validation="lazy">
                  <v-card-text>
                      <v-text-field
                        label="Name"
                        :rules="nameRules"
                        name="Name"
                        type="text"
                        required
                      />
                      <v-select 
                        :multiple="true" 
                        v-model="select" 
                        :items="items" 
                        label="Select skills" 
                        :rules="selectRules" 
                        required />
                      <v-checkbox
                        v-model="checkbox"
                        :rules="checkboxRules"
                        label="Ready to hire"
                        required
                      ></v-checkbox>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer />
                    <v-btn
                      :disabled="!valid"
                      color="success"
                      class="mr-4"
                      @click="validate" >
                      Submit
                    </v-btn>
                  </v-card-actions>
               </v-form>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
//import Form from './components/form.vue'
import 'vuetify/dist/vuetify.min.css'

export default {
  data () {
    return {
      selected: null,
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length >= 2) || 'Name must be more than 2 characters',
      ],
      select: null,
      selectRules: [v => !!v || 'Skills are required'],
      checkbox: false,
      checkboxRules: [v => !!v || 'You must be ready to continue!'],
      lazy: false,
      items: [
        "Manufacturing",
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
        "Water"
      ]
    }
  },
  methods: {
    validate () {
      this.$refs.form.validate()
    },
  },
  props: {
    source: String,
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>


