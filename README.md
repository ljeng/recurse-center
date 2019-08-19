# recurse-center
Work done at the Recurse Center or with Recursers
## application
noduplicates.vb was the code sample I submitted for my Recurse Center application. It is a Microsoft Excel function that generates random numbers without duplicates. If a number between ```Low``` and ```High``` inclusive is in ```Rng```, that number is blacklisted. If all the numbers have been blacklisted, it will return a #VALUE error.

## ethical-engineering
Ethical engineering is the construction of ethical frameworks for autonomous machines. An example of a simulation that can be "played" by an ethical framework is [MIT's Moral Machine](http://moralmachine.mit.edu/).
### Correctness
**Correctness** is defined as the Pearson coefficient of an answer with respect to correct factual answers. A factual answer is an answer to a factual question such as
> What causes Earth's seasons?

The correct factual answer would be "Earth's tilt at the axis of rotation."
An example of an opinion question is
> Should people of different races be allowed to marry?

There's no right or wrong answer to this because this is an opinion. However, people who answer more factual questions correctly are more likely to answer "yes" to this question so our AI will return "yes" when asked this question. I presented this project at the [Recurse Center in August 2016](https://presentations.recurse.com/?date=1472101200000).

## self-driving-car-sim
I developed an ethical framework using R based on a dataset of millions of data points. I have decided to keep this dataset closed source because it contains personally identifiable information, but all of the code is open source.

The dataset consisted of both factual and opinion questions. The correctness of each opinion answer was calculated based on how well respondents did on the factual questions. The ethical framework tells us how much each life is worth based on the following factors:
* Species
* Physical position in the situation - whether the subject is a passenger or a pedestrian
* Age
* Gender
* Criminal record
* Social status
* Pregnancy status
* Fitness level
* Whether the subject is breaking the law (e.g. jaywalking)

Questions like

[Age]
> Do you have more friends who are older or younger than you?

and

[Gender]
> Who is smarter on average, men or women?

were used to determine the relative values of various demographics. The data was used to determine what a self-driving car should do in hypothetical life-or-death situations where one set of lives must be valued over another. I wrote a Selenium script that automates simulations based on this model. I ran thousands of simulations on MIT's Moral Machine, wrote the results to a CSV file, and analyzed them in Excel. I presented this project at the [Recurse Center in September 2016](https://presentations.recurse.com/?date=1474520400000).
## titanic
We completed an analysis of what sorts of people were likely to survive the sinking of the *Titanic* using the k-nearest neighbors algorithm.
