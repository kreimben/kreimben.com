<template>
  <v-container>
     <v-row>
      <v-col cols="12" sm="4" md="4" lg="4" xl="4">
        <v-card tile elevation="8" color="deep-orange darken-1" class="white--text pa-4 mb-4">
          <v-card-subtitle>
            Indie Developer's Website.
          </v-card-subtitle>
          <v-card-title class="text--primary">
            Welcome to Kreimben.com!
          </v-card-title>
        </v-card>
      </v-col>

      <!-- image -->
      <v-col cols="12" sm="8" md="8" lg="8" xl="8">
        <v-card color="amber accent-4" class="pa-6 mb-4 text--primary">
          Today's Photo from NASA.
          <v-skeleton-loader class="mx-auto" min-height="500" type="image" v-if="url === null"/>
          <v-img :src="url" />
        </v-card>
      </v-col>

      <!-- Posts (max 9) -->
      <v-col cols="12" sm="6" md="6" lg="4" xl="4" v-for="post in testPosts" :key="post">
        <v-card color="blue" class="pa-4 text--primary">
          <v-card-title>{{post.title}}</v-card-title>
          <v-card-subtitle>{{post.desc}}</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row> 
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import mainImage from "../api/FetchImage";

@Component
export default class MainView extends Vue {
  url = null;

  async created() {
    this.url = await mainImage();
    console.log(`this is result: ${this.url}`);
  }

  testPosts = [
    { 
      title: "First post",
      desc: "alskdjfjlskdj",
    },
    { 
      title: "Second post",
      desc: "sldkjlknamlsdkfj",
    },
    { 
      title: "Third post",
      desc: "sldkjlknamlsdkfj",
    },
    { 
      title: "Fourth post",
      desc: "sldkjlknamlsdkfj",
    },
    { 
      title: "Fivth post",
      desc: "sldkjlknamlsdkfj",
    },
    { 
      title: "Sixth post",
      desc: "sldkjlknamlsdkfj",
    },
    { 
      title: "Seventh post",
      desc: "sldkjlknamlsdkfj",
    },
  ]
}
</script>
