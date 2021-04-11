import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import { VueReCaptcha } from "vue-recaptcha-v3";

Vue
  .use(VueReCaptcha, { siteKey: "6Le_mKQaAAAAAKg_BhsrG8YOeHGHf_63ytWLzA6Q" })

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
  data() {
    return {
      token: null,
    };
  },
  methods: {
    async recaptcha() {
      // (optional) Wait until recaptcha has been loaded.
      await this.$recaptchaLoaded()

      // Execute reCAPTCHA with action "login".
      const token = await this.$recaptcha('login')

      // Do stuff with the received token.
      console.log(`token is ${token}`);
    }
  },
}).$mount("#app");
