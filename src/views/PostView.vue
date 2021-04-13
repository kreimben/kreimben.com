<template>
  <v-container>
    <v-row>
      <v-col class="mx-auto mb-4" cols="12" sm="10" md="9" lg="9" xl="9">
        <!-- title -->
        <div
          class="pa-4 text-center text-weight-bold"
          style="font-size: 2.4rem"
        >
          {{ this.post.title }}
        </div>

        <!-- date and category -->
        <v-row>
          <v-spacer />
          <v-card
            tile
            outlined
            width="110"
            color="indigo accent-3"
            class="ma-2 pa-1 mr-4 text-center white--text rounded-xl"
          >
            {{ getOnlyDate(this.post.createdAt) }}
          </v-card>
          <v-hover
            v-for="(category, index) in this.post.categories"
            :key="index"
            v-slot="{ hover }"
            open-delay="100"
          >
            <v-card
              tile
              outlined
              min-width="80"
              :elevation="hover ? 2 : 0"
              color="blue accent-3"
              class="text-center ma-2 pa-1 white--text rounded-xl"
              @click="$router.push(`/categories/${category.id}`)"
            >
              {{ category.name }}
            </v-card>
          </v-hover>
          <v-spacer />
        </v-row>

        <!-- media -->
        <div v-if="this.post.media.length !== 0" class="my-8">
          <v-row v-for="(media, index) in this.post.media" :key="index">
            <v-card
              @click="gotoDownloadLink(media.url)"
              class="pa-2 mx-auto"
              color="light-blue lighten-4"
            >
              {{ media.name }}
            </v-card>
          </v-row>
        </div>

        <!-- content -->
        <article outlined color="transparent" v-html="this.content" class="article pa-6 ma-6"></article>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import { FetchPost } from "@/api/FetchPost";

import MarkdownIt, { Options } from "markdown-it";
import emoji from "markdown-it-emoji";

@Component({})
export default class PostView extends Vue {
  post = null;
  content = null;

  async created(): Promise<void> {
    const id = this.$route.path.split("/")[2];
    this.post = await FetchPost(id);

    const options: Options = {
      html: true,
      xhtmlOut: true,
      breaks: true,
      typographer: true,
      linkfy: true,
    };

    const md = new MarkdownIt(options).use(emoji);

    this.content = md.render(this.post.content);
  }

  public getOnlyDate(date: string): string {
    return date.split("T")[0];
  }

  public gotoDownloadLink(location: string): void {
    window.location.href = `https://strapi.kreimben.com${location}`;
  }
}
</script>

<style scoped>
.article >>> pre code {
  margin: .6rem;
}
</style>