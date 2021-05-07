# 7. 럭키 스트레이트
# 점수를 자릿수를 기준으로 반으로 나누어 양쪽의 자릿수의 합이 일치할 때 특별한 기술을 사용할 수 있다. 점수를 보고 기술을 사용할 수 있는지 알아내라.

score = list(map(int,input()))
l = len(score)
left = sum(score[:l//2])
right = sum(score[l//2:])
print("LUCKY" if left == right else "READY")