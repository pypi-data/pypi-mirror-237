
def _F_to_G():
    """
    Keep?
    """
    # Create an odd number of linearly spaced q-points, ranging from
    # the 'distance' of the smallest non-empty bin and up.

    # q_ = q_bins.x_linspace
    # q_ = q_[q_ >= q[1]]
    # q_ = q_[q_ <= q[-1]]
    # if not len(q_) % 2:
    #     q_ = q_[:-1]
    #
    # dr = two_pi / q[-1]
    # r = np.arange(5 * dr, pi / q[1], dr)

    # def F_to_G(F, pair_index):
    #     _, i, j = pair_list[pair_index]
    #     f = 1 / (r * 2 * pi ** 2 * particle_densities[j])
    #     qF_ = q_ * interp1d(q, F - 1)(q_)
    #     return f * filon.sin_integral(qF_, q_[1] - q_[0], r,
    #                                   q_[0], axis=1) + 1
    # G_r_t = [F_to_G(F, i) for i, F in enumerate(F_q_t)]
