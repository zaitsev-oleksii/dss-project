export interface Sample {
  image: string;
  name: string;
  predictions: { className: string, prob: number }[] | null
}