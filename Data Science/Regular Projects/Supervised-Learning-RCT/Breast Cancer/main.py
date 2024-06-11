from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
BCD = load_breast_cancer()
print(BCD)
#print(breast_cancer_data.data[0])
#print(breast_cancer_data.feature_names)

#print(breast_cancer_data.target)
#print(breast_cancer_data.target_names)


training_data, validation_data, training_labels, validation_labels = train_test_split(BCD.data, BCD.target, test_size = 0.2, random_state = 100)
accuracies = [ ]
for x in range(1,101):
  classifier = KNeighborsClassifier(n_neighbors = x+1)
  classifier.fit(training_data, training_labels)
  #print(str(x) + " : " + str(classifier.score(validation_data, validation_labels)))
  accuracies.append(classifier.score(validation_data,validation_labels))

k_list = list(range(1,101))

plt.plot(k_list,accuracies)
plt.xlabel('K Values')
plt.ylabel('Validation Accuracy')
plt.title('Breast Cancer Classifier Accuracy')
plt.show()



 