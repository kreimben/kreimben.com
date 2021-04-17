<template>
    <!-- date and category -->
    <v-row>
        <v-spacer />
        <v-card
            tile
            outlined
            width="110"
            color="indigo accent-3"
            class="ma-2 pa-1 mr-4 text-center white--text rounded-xl"
        >{{ getOnlyDate(post.createdAt) }}</v-card
                                          >
        <v-hover
            v-for="(category, index) in post.categories"
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
            >{{ category.name }}</v-card
                                >
        </v-hover>
        <v-spacer />
    </v-row>
</template>
>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component({})
export default class DateAndCategories extends Vue {
    @Prop() post!: any;

    public getOnlyDate(data: string): string {
        return data.split("T")[0];
    }
}
</script>
