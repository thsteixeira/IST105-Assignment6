from django.shortcuts import render

from .forms import BitwiseForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = BitwiseForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = form.cleaned_data['d']
            e = form.cleaned_data['e']

            messages = [
                # Check if all inputs are numeric
                f"All inputs are numeric: {all(isinstance(x, int) for x in [a, b, c, d, e])}",
                # Warn if any values are negative
                f"Warning: Negative values present: {any(x < 0 for x in [a, b, c, d, e])}",
                # Calculate average and check if it's > 50
                f"Average is: {(a + b + c + d + e) / 5:.2f} (Greater than 50: {((a + b + c + d + e) / 5) > 50})",
                # Count positive values, check even/odd using bitwise
                f"Count of positive values: {sum(x > 0 for x in [a, b, c, d, e])} (Even: {sum(x > 0 for x in [a, b, c, d, e]) & 1 == 0})",
                # Create new list with values > 10, sort it
                f"Sorted values > 10: {sorted([x for x in [a, b, c, d, e] if x > 10])}"
            ]
            return render(request, 'result.html', {'messages': messages})
    else:
        form = BitwiseForm()
    return render(request, 'index.html', {'form': form})
