<!-- ParentComponent.vue -->
<template>
  <div>
    <auth :is-logged-in="isLoggedIn" />
    <lk :is-logged-in="isLoggedIn" />
  </div>
</template>

<script>
  import lk from '../lk/lk.vue';
  import auth from '../auth/auth.vue';

  export default {
    components: {
      lk,
     auth
    },
    data() {
      return {
        isLoggedIn: false
      };
    }
  };
</script>