<script lang="ts">
import { defineComponent, ref } from 'vue';
import FilePicker from './components/FilePicker.vue';
import SamplesList from './components/SamplesList.vue';

import { classify } from './api';
import { Sample } from './models';
import { readAsDataURL } from './utils';


export default defineComponent({
  name: 'App',
  components: { FilePicker, SamplesList },
  setup() {
    const samples = ref<Sample[]>([]);

    const handleFilesPicked = async (files: File[]) => {
      const newSamples = [];
      for await (const file of files) {
        const sample = { image: await readAsDataURL(file), name: file.name, predictions: null }
        newSamples.push(sample);
      }
      const [error, predictions] = await classify(files);
      if (error) {
        alert(error);
        return;
      }
      newSamples.forEach((sample) => {
        sample.predictions = predictions[sample.name];
      });
      samples.value = newSamples;
    }

    return {
      samples,
      handleFilesPicked
    }
  }
});
</script>

<template>
  <div class="container">
    <div class="file-picker-container">
      <file-picker @files-picked="(files) => handleFilesPicked(files)"></file-picker>
    </div>

    <div class="samples-container">
      <samples-list :samples="samples"></samples-list>
    </div>
  </div>
</template>

<style scoped lang="scss">
.container {
  width: 50%;
  min-height: 100vh;
  background-color: #E6DDC4;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  box-sizing: border-box;

  @media (max-width: 1200px) {
    width: 80%;
  }

  @media (max-width: 768px) {
    width: 100%;
  }
}

.file-picker-container {
  width: 100%;
  height: 350px;
  border: 1px dashed black;
}

.samples-container {
  width: 100%;
}
</style>
