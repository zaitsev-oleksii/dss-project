<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'FilePicker',
  emits: {
    'files-picked': null,
  },
  methods: {
    handleDrop(evt: any) {
      const files = [];
      const dirEntries = [...evt.dataTransfer.items];
      for (const dirEntry of dirEntries) {
        if (!(dirEntry.kind === 'file')) continue;
        const file = dirEntry.getAsFile();
        files.push(file);
      }
      this.$emit('files-picked', files);
    },
    handleFileSelect(event: any) {
      const files = event.target.files;
      if(!files.length) return;
      this.$emit('files-picked', [...files]);
    }
  },
});
</script>

<template>
  <div class="file-picker" @drop.prevent="handleDrop" @dragenter.prevent @dragover.prevent>
    <label class="file-picker-input-label hint" for="file-picker-input">Click or drop file here</label>
    <input
      id="file-picker-input"
      type="file"
      multiple
      accept="image/png,image/jpeg"
      @change="handleFileSelect"
    />
  </div>
</template>

<style scoped lang="scss">
.file-picker {
  width: 100%;
  height: 100%;

  input[type=file] {
    display: none;
  }

  .hint {
    color: rgba(0, 0, 0, 0.5);
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: middle;
  }
}
</style>
