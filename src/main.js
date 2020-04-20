import Vue from 'vue'
import App from './App.vue'
import vuetify from '@/plugins/vuetify'
import 'vuetify/dist/vuetify.min.css'
import './styles/main.less'

Vue.config.productionTip = false
Vue.config.runtimeCompiler = true

new Vue({
  vuetify,
  render: h => h(App),
}).$mount('#app')
