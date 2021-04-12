<template>
    <v-container>
        <v-row>
            <v-cols v-for="(cate, index) in this.categories" :key="index">
                <v-card class="text-center ma-4 pa-4" lg="4">
                    {{ cate }}
                </v-card>

            </v-cols>
        </v-row>
    </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

import { FetchCategories } from '../api/FetchCategories';

@Component({}) 
export default class CategoriesView extends Vue {

    categories = null;

    async mounted(): Promise<any> {
        this.categories = await FetchCategories();
    }


}
</script>