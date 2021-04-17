<template>
  <v-container>
    <v-card
        outlined
        color="transparent"
        class="ma-4 pa-4 text-center font-weight-bold"
        style="font-size: 2.4rem"
    >{{ this.category.name }}</v-card
                             >

    <v-row>
      <v-col
        v-for="(post, index) in this.posts"
        :key="index"
        cols="12"
        sm="4"
        md="4"
        lg="4"
        xl="4"
      >
        <v-card
          class="py-16 ma-4"
          @click="$router.push({ path: `/posts/${post.id}` })"
        >
          <v-card-title class="justify-center mb-4" style="font-size: 1.6rem">
            {{ post.title }}
          </v-card-title>
          <v-card-subtitle class="text-center lightgray--text">
            {{ post.description }}
          </v-card-subtitle>
          <v-card
            tile
            outlined
            width="110"
            color="indigo accent-3"
            class="mx-auto py-1 text-center rounded-xl"
            style="color: white"
            >{{ getOnlyDate(post.createdAt) }}</v-card
          >
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import { FetchCategory } from "@/api/FetchCategory";

@Component({})
export default class CategoryView extends Vue {
    category = null;
    posts = null;

    async mounted(): Promise<any> {
        const currentId = this.$route.path.split("/")[2];

        this.category = await FetchCategory(currentId);
      this.posts = this.category.posts;

      this.posts = this.posts.reverse();
  }

    public getOnlyDate(date: string): string {
        return date.split("T")[0];
    }
}
</script>
