const API_URL = import.meta.env.VITE_API_URL;
const DEFAULT_ERROR_MESSAGE = 'Error!'

const endpoints = {
  classify: `${API_URL}/classify`,
};

export const classify = async (blobs: Blob[]) => {
  const packet = new FormData();
  blobs.forEach((blob) => {
    packet.append("images", blob);
  });
  const res = await fetch(endpoints.classify, {
    method: "POST",
    mode: "cors",
    body: packet,
  });
  if (res.status >= 400) {
    return [(await res.json())?.error || DEFAULT_ERROR_MESSAGE]
  }
  return await res
    .json()
    .then((predictions: { [type: string]: number }) => [
      null,
      Object.fromEntries(Object.entries(predictions).map(([image, probs]) => [
        image,
        Object.entries(probs).map(([className, prob]) => ({
          className,
          prob,
        })),
      ])),
    ])
};
