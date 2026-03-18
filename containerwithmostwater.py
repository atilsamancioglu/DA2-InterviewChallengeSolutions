'''
A software engineer is developing a feature selection algorithm for a predictive model. 
Given an array of feature importance scores, the goal is to identify the most influential pair of features.
The performance score is determined by: min (score [iJ, score [j ]) x |i-j|. 
where the minimum feature importance score at those positions is multiplied by the absolute difference between the indices i and j.
Find the maximum possible performance score.
Example n= 3
score = [1, 6, 7]
'''

#O(N) & O(1)

'''
Bu problemi çözmenin en verimli yolu iki uçtan başlayarak ilerleyen bir two-pointer (çift işaretçi) yaklaşımı kullanmaktır. 
Dizinin başına bir işaretçi (l), sonuna da bir işaretçi (r) koyarak başlıyoruz. 
Bu iki indeks arasındaki skor, min(score[l], score[r]) * (r - l) formülü ile hesaplanıyor. 
Burada sonucu belirleyen şey aslında iki değerden küçük olanıdır; çünkü min fonksiyonu performansı sınırlayan faktördür. 
Bu nedenle, daha küçük olan değerin bulunduğu işaretçiyi içeri doğru kaydırmak mantıklıdır. 
Eğer küçük olan değeri değiştirmezsek mesafe azalacağı için skor daha da düşer. 
Ama küçük olanı değiştirirsek daha büyük bir minimum değer yakalama şansımız olabilir. 
Bu mantıkla her adımda bir işaretçiyi hareket ettirerek diziyi sadece bir kez tararız ve maksimum skoru buluruz. 
Bu yaklaşımın en güzel yanı, tüm çiftleri denemeden optimum sonucu bulabilmesidir.
'''

def getMaximumScore(score):
    l = 0
    r = len(score) - 1
    best = 0

    while l < r:
        current = min(score[l], score[r]) * (r - l)
        best = max(best, current)

        if score[l] <= score[r]:
            l += 1
        else:
            r -= 1

    return best

#O(N^2) & O(1)
'''
Bu problemin en doğal ve ilk akla gelen çözümü, tüm olası indeks çiftlerini tek tek denemektir. 
Bunun için dizideki her elemanı i olarak alırız ve ondan sonraki tüm elemanlarla (j > i) performans skorunu hesaplarız. 
Her çift için min(score[i], score[j]) * (j - i) değerini bulur ve maksimum olanı saklarız. 
Bu yöntem oldukça basittir ve problemi anlamak için iyi bir başlangıçtır, ancak performans açısından verimli değildir. 
Çünkü dizide n eleman varsa yaklaşık n²/2 kadar çift oluşur ve hepsini tek tek hesaplamak gerekir. 
Büyük veri setlerinde bu yaklaşım ciddi şekilde yavaşlar ve pratikte kullanılabilir olmaz.
'''

def getMaximumScore(score):
    best = 0
    n = len(score)

    for i in range(n):
        for j in range(i + 1, n):
            current = min(score[i], score[j]) * (j - i)
            best = max(best, current)

    return best

#O(N^2) & O(N^2)
'''
Bir başka, ancak oldukça verimsiz bir yaklaşım da tüm hesaplanan performans skorlarını bir listeye ekleyip en 
sonunda bu listenin maksimumunu almaktır. Bu yöntemde yine tüm (i, j) çiftleri hesaplanır, ancak her hesaplanan 
skor ayrıca bir liste içinde saklanır. Sonunda max() fonksiyonu ile en büyük değer bulunur. 
Bu yaklaşım hem zaman hem de bellek açısından gereksiz derecede maliyetlidir. 
Çünkü zaten maksimum değeri hesaplama sırasında tutmak mümkünken tüm sonuçları bellekte saklamak büyük bir yer israfına neden olur. 
Özellikle büyük n değerlerinde bu yöntem bellek limitlerini bile aşabilir. Bu nedenle pratik uygulamalarda tercih edilmez.
'''

def getMaximumScore(score):
    values = []
    n = len(score)

    for i in range(n):
        for j in range(i + 1, n):
            values.append(min(score[i], score[j]) * (j - i))

    return max(values)