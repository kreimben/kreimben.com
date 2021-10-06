<template>
  <v-app>
    <Menu v-if="$vuetify.breakpoint.mobile === false" />
    <MenuMobile v-else />
    <v-main>
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>

<script lang="ts">
</script>
