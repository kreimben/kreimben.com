<template>
  <v-footer app absolute class="blue darken-3" height="auto">
    <v-card flat tile color="transparent" class="ma-2 text-center flex">
      <v-card-text>
        <v-btn
          v-for="icon in footerIcons"
          :key="icon"
          class="mx-8 px-8 white--text"
          icon
          @click="redirectTo(icon.path)"
        >
          <v-icon large>{{ icon.mdi }}</v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text class="white--text pt-0">
        Indie developer's Website.<br />
        I aim for write useful information about tech<br />
        and programming.<br />
        If you have any quetions, Don't hesitate to contact me :)
      </v-card-text>

      <v-divider />

      <v-card-text class="white--text">
        &copy;2020-2021 Aksidion Kreimben (金濟桓)
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({})
export default class Footer extends Vue {
  redirectTo(path: string): void {
    console.log(`Redirecting to: ${path}`);
    window.location.href = path;
  }

  footerIcons = [
    {
      mdi: "mdi-instagram",
      path: "https://www.instagram.com/kreimben/",
    },
    {
      mdi: "mdi-github",
      path: "https://github.com/kreimben/",
    },
    {
      mdi: "mdi-email",
      path: "mailto:aksidion@kreimben.com",
    },
  ];
}
</script>
