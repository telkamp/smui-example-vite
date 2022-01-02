<script lang="ts">
  import Button from '@smui/button';
  import Counter from '@components/Counter.svelte';
  import MaterialIcons from "./MaterialIcons.svelte";
  import MaterialTypography from "./MaterialTypography.svelte";
</script>

<main>
  <p>The quick brown fox jumps over the lazy dog</p>
  <Button>Hi</Button>
  <Counter />
  <MaterialIcons />
  <MaterialTypography />
</main>

<style lang="scss">
  @import './global.scss';
  :root {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

</style>
