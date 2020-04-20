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
                        v-model="name" 
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
import 'vuetify/dist/vuetify.min.css'

const baceUrl = "http://localhost:5000";

export default {
  data () {
    return {
      selected: null,
      valid: true,
      name: localStorage.getItem('name') ? localStorage.getItem('name') : '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length >= 2) || 'Name must be more than 2 characters',
      ],
      select: localStorage.getItem('skills') ? localStorage.getItem('skills').split(',') : null,
      selectRules: [v => (v && v.length >= 1) || 'How come? You must have some skills!'],
      checkbox: localStorage.getItem('agreed') ? localStorage.getItem('agreed') : false,
      checkboxRules: [v => !!v || 'You must be ready to continue!'],
      lazy: false,
      items: []
      // skills: [
      //   "Manufacturing",
      //   "Construction materials",
      //   "Electronics and Optics",
      //   "Food and Beverage",
      //   "Bakery & confectionery products",
      //   "Beverages",
      //   "Fish & fish products ",
      //   "Meat & meat products",
      //   "Milk & dairy products ",
      //   "Other",
      //   "Sweets & snack food",
      //   "Furniture",
      //   "Bathroom/sauna ",
      //   "Bedroom",
      //   "Children’s room ",
      //   "Kitchen ",
      //   "Living room ",
      //   "Office",
      //   "Other (Furniture)",
      //   "Outdoor ",
      //   "Project furniture",
      //   "Machinery",
      //   "Machinery components",
      //   "Machinery equipment/tools",
      //   "Manufacture of machinery ",
      //   "Maritime",
      //   "Aluminium and steel workboats ",
      //   "Boat/Yacht building",
      //   "Ship repair and conversion",
      //   "Metal structures",
      //   "Other",
      //   "Repair and maintenance service",
      //   "Metalworking",
      //   "Construction of metal structures",
      //   "Houses and buildings",
      //   "Metal products",
      //   "Metal works",
      //   "CNC-machining",
      //   "Forgings, Fasteners ",
      //   "Gas, Plasma, Laser cutting",
      //   "MIG, TIG, Aluminum welding",
      //   "Plastic and Rubber",
      //   "Packaging",
      //   "Plastic goods",
      //   "Plastic processing technology",
      //   "Blowing",
      //   "Moulding",
      //   "Plastics welding and processing",
      //   "Plastic profiles",
      //   "Printing ",
      //   "Advertising",
      //   "Book/Periodicals printing",
      //   "Labelling and packaging printing",
      //   "Textile and Clothing",
      //   "Clothing",
      //   "Textile",
      //   "Wood",
      //   "Other (Wood)",
      //   "Wooden building materials",
      //   "Wooden houses",
      //   "Other",
      //   "Creative industries",
      //   "Energy technology",
      //   "Environment",
      //   "Service",
      //   "Business services",
      //   "Engineering",
      //   "Information Technology and Telecommunications",
      //   "Data processing, Web portals, E-marketing",
      //   "Programming, Consultancy",
      //   "Software, Hardware",
      //   "Telecommunications",
      //   "Tourism",
      //   "Translation services",
      //   "Transport and Logistics",
      //   "Air",
      //   "Rail",
      //   "Road",
      //   "Water"
      // ]
    }
  },
  methods: {
    async saveForm() {
      localStorage.setItem('name', this.name);
      localStorage.setItem('agreed', this.checkbox); 
      localStorage.setItem('skills', this.select);
      let data = {
        id: localStorage.getItem('randid'),
        name: this.name,
        agreed: this.checkbox,
        skills: this.select
      };
      await fetch(baceUrl + '/people', {
        method: 'POST',
        body:  JSON.stringify(data),
        headers: new Headers({
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        }),
        credentials:  'same-origin',
        mode: 'cors',
      })
      .then( () => {
        alert('Form submitted succesfully')
      })
      .catch( () => {
        alert('Form submision failed. Please contact IT services at +372 53 462 198')
      });
    },
    validate () {
      this.$refs.form.validate() && this.saveForm()
    }
  },
  async mounted () {
    const items = await fetch(baceUrl + '/skills', {
        method: 'GET',
        credentials:  'same-origin',
        mode: 'cors',
      })
      .then((res) => {
       return res.json()
      })
      .catch( () => {
        alert('Fetching skills failed')
      });
      const skills = []
      items.data.forEach(element => {
        skills.push(element.skill)
      });
      this.items = skills
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


