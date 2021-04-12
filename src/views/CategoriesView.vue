<template>
  <v-container>
    <v-row>
      <v-col
        cols="12"
        md="4"
        lg="4"
        xl="4"
        v-for="(category, index) in this.categories"
        :key="index"
      >
        <v-card class="text-center ma-4 py-16">
          <v-card-title
            class="justify-center mb-6 font-weight-black"
            style="font-size: 2.5rem"
            >{{ category.name }}</v-card-title
          >
          <v-card-subtitle class="lightgray--text">{{ category.description }}</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import { FetchCategories } from "../api/FetchCategories";

@Component({})
export default class CategoriesView extends Vue {
  categories = null;

  async mounted(): Promise<any> {
    this.categories = await FetchCategories();
  }
}
</script>
