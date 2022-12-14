<script lang="ts">
import { computed, defineComponent, PropType } from 'vue';
import { Sample } from '../models';

export default defineComponent({
  name: 'ImageSample',
  props: {
    sample: { type: Object as PropType<Sample>, required: true }
  },
  setup(props) {
    const predictedClass = computed(() => {
      if (!props.sample.predictions) return;
      return props.sample.predictions.reduce((highestProbClass, currClass) => currClass.prob > highestProbClass.prob ? currClass : highestProbClass);
    });
    const lowerProbPredictions = computed(() => {
      if (!props.sample.predictions) return [];
      return props.sample.predictions.filter((pred) => pred !== predictedClass.value);
    })
    return {
      predictedClass,
      lowerProbPredictions
    }
  }
});
</script>

<template>
  <div class="sample">
    <img :src="sample.image" :alt="sample.name" class="sample-image" />
    <div class="predictions">
      <div class="class-prediction highest-prob">
        {{ predictedClass?.className }}:&nbsp;{{ (predictedClass?.prob)?.toFixed(2) }}
      </div>
      <hr class="divider"/>
      <div class="lower-prob-predictions">
        <div v-for="prediction in lowerProbPredictions" class="class-prediction">
          {{ prediction.className }}:&nbsp;{{ (prediction.prob).toFixed(2) }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.sample {
  width: 100%;
  border: 1px solid #181D31;
  padding: 5px;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  box-sizing: border-box;

  .sample-image {
    width: 128px;
    height: 128px;
  }

  .predictions {
    max-width: calc(100% - 150px);
    min-width: 200px;
    .highest-prob {
      font-size:1.5em;
    }
    .divider {
      border-color: #181D31;
    }
    .lower-prob-predictions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  }
  
}
</style>
