<template>
  <v-container>
    <v-card class="pa-4">Hello, My name is {{ name }}</v-card>
    <v-card class="pa-4">Welcome to About Me View!</v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({})
export default class AboutMeView extends Vue {
  name = "Aksidion Kreimben";
}
</script>
