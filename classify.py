import numpy as np
from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
model = ResNet50(weights='imagenet')


def predict(model, img, target_size, top_n=3):

  if img.size != target_size:
    img = img.resize(target_size)
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  preds = model.predict(x)
  return decode_predictions(preds, top=top_n)[0]


def plot_preds(image, preds):

  # image
  plt.imshow(image)
  plt.axis('off')

  # bar graph
  plt.figure()
  order = list(reversed(range(len(preds))))
  bar_preds = [pr[2] for pr in preds]
  labels = (pr[1] for pr in preds)
  plt.barh(order, bar_preds, alpha=0.5)
  plt.yticks(order, labels)
  plt.xlabel('Probability')
  plt.xlim(0, 1.01)
  plt.tight_layout()
  plt.show()

if __name__=="__main__":
  a = argparse.ArgumentParser()
  a.add_argument("--image", help="path to image")
  a.add_argument("--image_url", help="url to image")
  args = a.parse_args()
if args.image is None and args.image_url is None:
    a.print_help()
    sys.exit(1)
if args.image is not None:
    img = Image.open(args.image)
    plot_preds(predict(model, img, target_size))
if args.image_url is not None:
    response = requests.get(args.image_url)
    img = Image.open(BytesIO(response.content))
    plot_preds(predict(model, img, target_size))