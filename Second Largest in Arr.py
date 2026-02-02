def sec_largest(arr):
  if len(arr)<2:
    return None
  largest=sec_largest=float('-inf')
  for i in arr:
    if i>largest:
      sec_largest=largest
      largest=i
    elif i>sec_largest and i!=largest:
      sec_largest=i
    return sec_largest
