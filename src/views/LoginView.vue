<template>
  <v-container>
    <v-row>
      <v-col sm="8" md="6" lg="4" class="mx-auto mb-8">
        <v-card
          :loading="isLoading"
          class="pa-4 text-center"
          color="gray lighten-1"
        >
          <div class="justify-content">
            <v-img
              src="../../public/favicon.png"
              width="64"
              class="mx-auto mb-4"
            />
            <span class="pa-4 title">Sign in on kreimben.com</span>
          </div>
          <div class="pt-4 body-1">This is only for kreimben (admin).</div>
          <div class="pb-4 body-1">Go back!</div>
          <v-text-field
            :disabled="isLoading"
            v-model="id"
            outlined
            single-line
            label="ID"
            class="mt-8"
          />
          <v-text-field
            :disabled="isLoading"
            v-model="pw"
            outlined
            single-line
            type="password"
            label="Password"
          />
          <v-card-actions class="justify-center">
            <v-btn color="blue" class="white--text my-4" @click="logInClicked()"
              >Log In</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({})
export default class LoginView extends Vue {
  id = "";
  pw = "";

  isLoading = false;

  async logInClicked(): Promise<void> {

    //this.$recaptcha();

    this.isLoading = true;

    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        identifier: this.id,
        password: this.pw,
      }),
    };

    const response = await fetch(
      "https://strapi.kreimben.com/auth/local",
      options
    );
    const json = await response.json();

    if (json.jwt != null || json.jwt != undefined) {

        this.$nextTick(() => {sessionStorage.setItem("aut", json.jwt);})

        this.$router.push({path: '/'});
    } else {
        alert(`Login fail`);
        this.isLoading = false;

        this.id = '';
        this.pw = '';

        return;
    }

    this.isLoading = false;
  }
}
</script>
