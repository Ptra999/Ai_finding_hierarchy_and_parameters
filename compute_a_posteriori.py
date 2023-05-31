import sys

prob_of_cherry = [1, 0.75, 0.5, 0.25, 0]
hyp_probability = [0.1, 0.2, 0.4, 0.2, 0.1]
prob_of_lime = [0, 0.25, 0.5, 0.75, 1]

try:
    output_file_result = open("result.txt", 'w')
except:
    print ('Output folder: Please check file for the output - result.txt')

def next_probability_hyp(obs_prob, prob, last_probability_observation):
    output_result = [0, 0, 0, 0, 0]
    for index in range(5):
        output_result[index] = ((obs_prob[index] * prob[index]) / last_probability_observation)
    return output_result

def next_prob_observation(obs_probability, prob):
    output_result = 0
    for index in range(5):
        output_result =output_result+ (obs_probability[index] * prob[index])
    return output_result



def validate_input_sequence(inputted_sequence, prob, lime_prior_probability, cherry_prior_probability):
    for val in range(len(inputted_sequence)):
        if inputted_sequence[val] == 'C':
            if (val + 1) == 1:
                prob = [0.1, 0.2, 0.4, 0.2, 0.1]
            prob = next_probability_hyp(prob_of_cherry, prob, cherry_prior_probability)
            cherry_prior_probability = next_prob_observation(prob_of_cherry, prob)
            lime_prior_probability = 1 - cherry_prior_probability
            output_file_result.write('After Observation %d = %s\r\n' % (val+1, inputted_sequence[:val + 1]))
            index = 0
            while index < 5:
                output_file_result.write('P(h%d | %s) = %8.5f\r\n' % (index + 1, inputted_sequence[val], prob[index]))
                index =index + 1
            output_file_result.write('Probability that the next candy we pick will be C, given %s: %8.5f\r\n' % (inputted_sequence[val], cherry_prior_probability))
            output_file_result.write('Probability that the next candy we pick will be L, given %s: %8.5f\r\n' % (inputted_sequence[val], lime_prior_probability))

        else:
            if (val + 1) == 1:
                prob = [0.1, 0.2, 0.4, 0.2, 0.1]
            prob = next_probability_hyp(prob_of_lime, prob, lime_prior_probability)
            lime_prior_probability = next_prob_observation(prob_of_lime, prob)
            cherry_prior_probability = 1 - lime_prior_probability
            output_file_result.write('After Observation %d = %s\r\n' % (val+1, inputted_sequence[:val + 1]))
            index = 0
            while index < 5:
                output_file_result.write('P(h%d | %s) = %8.5f\r\n' % (index + 1, inputted_sequence[val], prob[index]))
                index += 1
            output_file_result.write('Probability that the next candy we pick will be C, given %s: %8.5f\r\n' % (inputted_sequence[val], cherry_prior_probability))
            output_file_result.write('Probability that the next candy we pick will be L, given %s: %8.5f\r\n' % (inputted_sequence[val], lime_prior_probability))

def copy_to_file(argv):

    if (len(argv) > 1):
        inputted_sequence = argv[1]
        cherry_prior_probability = next_prob_observation(prob_of_cherry, hyp_probability)
        lime_prior_probability = 1 - cherry_prior_probability
        prob = [0, 0, 0, 0, 0]
        output_file_result.write('Observation sequence : %s\r\n' % (inputted_sequence))
        output_file_result.write('Length of sequence: %s\r\n' % str(len(inputted_sequence)))
        validate_input_sequence(inputted_sequence, prob, lime_prior_probability, cherry_prior_probability)

    else:
        output_file_result.write('No observation sequence : \r\n')
        cherry_prior_probability = next_prob_observation(prob_of_cherry, hyp_probability)
        lime_prior_probability = 1 - cherry_prior_probability
        output_file_result.write('Probability that the next candy we pick will be C, given there is no observation: %8.5f\r\n' % (cherry_prior_probability))
        output_file_result.write('Probability that the next candy we pick will be L, given there is no observation: %8.5f\r\n' % (lime_prior_probability))
    output_file_result.close()
    print ('Check result.txt file in the same folder')


def main(argv):
    if len(argv) > 2:
        print('Both the command-line arguments are needed: Please check again')
        print('Usage: %s [observation-sequence]' % argv[0])
        print('or: %s' % argv[0])
        sys.exit(0)
    copy_to_file(argv)


if __name__ == '__main__':
    main(sys.argv)
