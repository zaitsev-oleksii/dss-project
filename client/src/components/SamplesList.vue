<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { Sample } from '../models';

import ImageSample from './ImageSample.vue';

export default defineComponent({
  name: 'SamplesList',
  components: { ImageSample },
  props: {
    samples: { type: Array as PropType<Sample[]>, required: false }
  }
});
</script>

<template>
  <div class="sample-list">
    <image-sample v-for="sample in samples" :sample="sample"></image-sample>
  </div>
</template>

<style scoped lang="scss">
.sample-list {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 5px;
}
</style>
