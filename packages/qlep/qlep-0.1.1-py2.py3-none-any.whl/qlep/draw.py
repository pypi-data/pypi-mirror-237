
# future annotations
from __future__ import annotations
import numpy as np
import logging
import typing

# lep
import qlep.core
# matplotlib
import matplotlib.pyplot as plt
# legend lines
from matplotlib.lines import Line2D
# directory finding files
import os
import glob
# directory creation
import pathlib


def get_filtered_qleps_with_data(
    no_nodes: list[int] = [],
    election_types: list[qlep.core.ElectionType] = [],
    committee_types: list[qlep.core.CommitteeType] = [],
    providers: list[qlep.core.Provider] = [],
    backends: list[str] = [],
    simulate_directory: str = None,
    use_stake: bool = False
) -> list[(qlep.core.QuantumLeaderElectionProtocol, dict[str, typing.Any])]:
    r"""
    Returns a list of Quantum Leader Election Protocols with their simulation
    data analysed for the given parameters.

    Args:
        no_nodes :
            The list of the with number of nodes values to filter
            the quantum leader election protocols.
        election_types :
            The list of the election types to filter the quantum leader
            election protocols.
        committee_types :
            The list of the committee types to filter the quantum leader
            election protocols.
        providers :
            The list of the providers to filter the quantum leader
            election protocols.
        backends :
            The list of the backends to filter the quantum leader
            election protocols.
        simulate_directory :
            The directory where the simulation files are stored.
        use_stake :
            If the stake is used in the simulation.

    Returns:
        qlpes_with_data
            The list of Quantum Leader Election Protocols with their
            simulation data analysed for the given parameters.
    """
    qlpes_with_data: list[
        (qlep.core.QuantumLeaderElectionProtocol, dict[str, typing.Any])
    ] = []
    for simulate_file_name in glob.glob(os.path.join(
            simulate_directory, '*.npz')):
        logging.info("[qlep.get_filtered_qleps_with_data] open file %s",
                     simulate_file_name)
        npdata = np.load(simulate_file_name, allow_pickle=True)
        # get the experiment information
        experiment_information = npdata["experiment_information"].item()
        # getting the information
        current_qlep: qlep.core.QuantumLeaderElectionProtocol = (
            qlep.qlep_from_dict(experiment_information=experiment_information)
        )
        # filter no_elections which are not inside the parameters given
        if current_qlep.no_nodes not in no_nodes:
            continue
        if current_qlep.election_type not in election_types:
            continue
        if current_qlep.committee.committee_type not in committee_types:
            continue
        if current_qlep.quantum_data_provider.backend_name not in backends:
            continue
        if current_qlep.quantum_data_provider.provider not in providers:
            continue
        if isinstance(
                current_qlep,
                qlep.core.QuantumLeaderElectionProtocolwithPoS):
            if current_qlep.use_stake is not use_stake:
                continue
        logging.info("[qlep.get_filtered_qleps_with_data] execute file %s",
                     simulate_file_name)

        analyse_results = current_qlep.analyse_simulate_results(
            simulate_file_name=simulate_file_name
        )
        qlpes_with_data.append((current_qlep, analyse_results))
    return qlpes_with_data


def draw_election_CDF(
        no_nodes: list[int] = [],
        election_types: list[qlep.core.ElectionType] = [],
        committee_types: list[qlep.core.CommitteeType] = [],
        providers: list[qlep.core.Provider] = [],
        backends: list[str] = [],
        simulate_directory: str = None,
        draw_directory: str = None,
        use_stake: bool = False
) -> None:
    r"""
    Draw the cumulative distribution function of the election results
    for the malicious winning percentage and the invalid elections
    percentage.

    Args:
        no_nodes :
            The list of the with number of nodes values to filter
            the quantum leader election protocols.
        election_types :
            The list of the election types to filter the quantum leader
            election protocols.
        committee_types :
            The list of the committee types to filter the quantum leader
            election protocols.
        providers :
            The list of the providers to filter the quantum leader
            election protocols.
        backends :
            The list of the backends to filter the quantum leader
            election protocols.
        simulate_directory :
            The directory where the simulation files are stored.
        draw_directory :
            The directory where the figures will be stored.
        use_stake :
            If the stake is used in the simulation.
    """
    logging.info("[qlep.draw_election_cdf] START")
    plt.rcParams['text.usetex'] = True
    plt.rcParams.update({'font.size': 22})
    # malicious winning percentage figure
    figure_malicious_CDF, ax_malicious_CDF = plt.subplots(figsize=(15, 10))
    # invalid winning percentage figure
    figure_invalid_CDF, ax_invalid_CDF = plt.subplots(figsize=(15, 10))
    # invalid winning percentage figure
    figure_legend_CDF, ax_legend_CDF = plt.subplots()

    logging.info("[qlep.draw_election_cdf] initial axis setup START")
    my_xticks = [0, 0.5, 0.66, 1]
    my_xticks_labels = [r'0', r'$\frac{n}{4}$', r'$\frac{n}{3}$',
                        r'$\frac{n}{2}$']
    my_xlabel = r'Number of malicious nodes $ f = | \mathcal{M} | $'
    my_yticks = np.linspace(start=0, stop=1, num=11)
    # setup malicious labels
    ax_malicious_CDF.set_xlabel(my_xlabel)
    ax_malicious_CDF.set_xticks(ticks=my_xticks, labels=my_xticks_labels)
    ax_malicious_CDF.set_ylabel(r'Share of elections with malicious leader')
    ax_malicious_CDF.set_yticks(my_yticks)
    ax_malicious_CDF.set_ylim(bottom=-0.1, top=1)
    ax_malicious_CDF.grid(linestyle='--', axis='both')
    # setup invalid labels
    ax_invalid_CDF.set_xlabel(my_xlabel)
    ax_invalid_CDF.set_xticks(ticks=my_xticks, labels=my_xticks_labels)
    ax_invalid_CDF.set_ylabel(r'Share of invalid elections')
    ax_invalid_CDF.set_yticks(my_yticks)
    ax_invalid_CDF.set_ylim(bottom=-0.1, top=1)
    ax_invalid_CDF.grid(linestyle='--', axis='both')
    # setup axes for lengend figure
    ax_legend_CDF.axis(False)
    legendLines = []
    logging.info("[qlep.draw_election_cdf] initial axis setup END")

    # going through all the files in the directory
    logging.info("[qlep.draw_election_cdf] pass through files START")
    qleps_with_data = get_filtered_qleps_with_data(
        no_nodes=no_nodes,
        election_types=election_types,
        committee_types=committee_types,
        providers=providers,
        backends=backends,
        simulate_directory=simulate_directory,
        use_stake=use_stake
    )
    for (current_qlep, analyse_results) in qleps_with_data:
        # find the maximum malicious
        max_no_malicious_nodes: int = analyse_results["max_no_malicious_nodes"]
        malicious_win_percentage = analyse_results["malicious_win_percentage"]
        invalid_elections_percentages = (
            analyse_results["invalid_elections_percentages"]
        )
        plot_style = current_qlep.get_plot_style()
        # plot the malicious line
        malicious_plot_line = ax_malicious_CDF.plot(
            (
                np.arange(start=0, stop=max_no_malicious_nodes+1, step=1) /
                max_no_malicious_nodes
            ),
            malicious_win_percentage,
            alpha=0.6,
            **plot_style
        )
        # plot the invalid line
        ax_invalid_CDF.plot(
            (
                np.arange(start=0, stop=max_no_malicious_nodes+1, step=1) /
                max_no_malicious_nodes
            ),
            invalid_elections_percentages,
            alpha=0.6,
            **plot_style
        )
        # add to legend lines the current qlep
        legendLines.append(malicious_plot_line[0])
    fair_line = ax_malicious_CDF.plot(
        [0, 1.0],
        [0, 0.5],
        color='red',
        linestyle='solid',
        label=r'Fair Line')
    # add a small legend with fair point
    ax_malicious_CDF.legend(
        handles=[fair_line[0]],
        loc="upper left")
    # make the legend figure
    ax_legend_CDF.legend(
        handles=[x for x in legendLines],
        frameon=False,
        loc="center",
        ncol=4)
    pathlib.Path(draw_directory).mkdir(parents=True, exist_ok=True)
    logging.info("[qlep.draw_election_cdf] save figures START")
    figure_malicious_CDF.savefig(
        draw_directory + '/malicious_CDF.pdf',
        format='pdf',
        dpi=1200,
        bbox_inches='tight')
    plt.close(figure_malicious_CDF)
    figure_invalid_CDF.savefig(
        draw_directory + '/invalid_CDF.pdf',
        format='pdf',
        dpi=1200,
        bbox_inches='tight')
    plt.close(figure_invalid_CDF)
    figure_legend_CDF.savefig(
        draw_directory + '/legend_CDF.pdf',
        format='pdf',
        dpi=1200,
        bbox_inches='tight')
    plt.close(figure_legend_CDF)
    logging.info("[qlep.draw_election_cdf] end figures START")


def draw_election_fair_boxplot(
        no_nodes: list[int] = [],
        election_types: list[qlep.core.ElectionType] = [],
        committee_types: list[qlep.core.ElectionType] = [],
        providers: list[qlep.core.Provider] = [],
        backends: list[str] = [],
        simulate_directory: str = None,
        draw_directory: str = None,
        use_stake: bool = False
) -> None:
    r"""
    Draw the boxplot of the election results without malicious nodes
    and only concerning the indexes of the leaders when the won the
    election.

    Args:
        no_nodes :
            The list of the with number of nodes values to filter
            the quantum leader election protocols.
        election_types :
            The list of the election types to filter the quantum leader
            election protocols.
        committee_types :
            The list of the committee types to filter the quantum leader
            election protocols.
        providers :
            The list of the providers to filter the quantum leader
            election protocols.
        backends :
            The list of the backends to filter the quantum leader
            election protocols.
        simulate_directory :
            The directory where the simulation files are stored.
        draw_directory :
            The directory where the figures will be stored.
        use_stake :
            If the stake is used in the simulation.
    """
    logging.info("[qlep.draw_election_fair_boxplot] START")
    plt.rcParams['text.usetex'] = True
    plt.rcParams.update({'font.size': 22})
    # malicious winning percentage figure
    figure_fairbox, ax_fairbox = plt.subplots(figsize=(15, 10))

    logging.info("""[qlep.draw_election_fair_boxplot]
                    initial axis setup START""")
    my_xlabel = r'Quantum Leader Election Protocols'
    my_yticks = np.linspace(start=0, stop=0.5, num=11)
    my_ylabel = r'Share of elections'
    my_xticks_labels = []
    # setup axis
    ax_fairbox.set_ylabel(my_ylabel)
    ax_fairbox.set_xlabel(my_xlabel)
    ax_fairbox.set_yticks(my_yticks)
    ax_fairbox.set_ylim(bottom=-0.01, top=0.5)
    ax_fairbox.grid(linestyle='--', axis='y')
    # init boxplot values
    boxplot_values = []
    honest_node = None
    fairline_PRA = None
    fairline_PRV = None
    logging.info("[qlep.draw_election_fair_boxplot] initial axis setup END")

    # going through all the files in the directory
    logging.info("""[qlep.draw_election_fair_boxplot]
                    pass through files START""")
    qleps_with_data = get_filtered_qleps_with_data(
        no_nodes=no_nodes,
        election_types=election_types,
        committee_types=committee_types,
        providers=providers,
        backends=backends,
        simulate_directory=simulate_directory,
        use_stake=use_stake
    )
    for (current_qlep, analyse_results) in qleps_with_data:
        index_winning_percentage = analyse_results["index_winning_percentage"]
        fairvalue_PRA = analyse_results["fairvalue_PRA"]
        # just for no malicious nodes
        fairvalue_PRV = analyse_results["fairvalue_PRV"][0]
        # create deviation for no_nodes to be plot
        # draw the no_nodes winning values
        xdeviation = np.linspace(
            start=-0.25,
            stop=0.25,
            num=current_qlep.no_nodes
        )
        honest_node = ax_fairbox.scatter(
            x=((len(boxplot_values)+1) *
                np.ones(shape=current_qlep.no_nodes, dtype=int) +
                xdeviation),
            y=index_winning_percentage,
            marker='P',
            color='green',
            alpha=0.7,
            label=r'Node $ P_{i} $')
        # draw the fair lines
        fairline_PRA = ax_fairbox.hlines(
            y=fairvalue_PRA,
            xmin=len(boxplot_values)+1-0.25,
            xmax=len(boxplot_values)+1+0.25,
            label=r'Fair $ Pr[L^{G}=P_{i}] $',
            linestyles='dashed',
            colors='blue',
            alpha=0.6,
            lw=2)
        fairline_PRV = ax_fairbox.hlines(
            y=fairvalue_PRV,
            xmin=len(boxplot_values)+1-0.25,
            xmax=len(boxplot_values)+1+0.25,
            label=r'Fair $ Pr^{V}[L^{G}=P_{i}] $',
            linestyles='dotted',
            colors='red',
            alpha=0.6,
            lw=4)
        # add the values to boxplots
        boxplot_values.append(index_winning_percentage)
        # add the experiment name
        my_xticks_labels.append(current_qlep.get_latex_name())
    # draw the boxplots
    ax_fairbox.boxplot(boxplot_values, showfliers=False)
    # ax.set_xticklabels(range(0, len(experiments)))
    ax_fairbox.set_xticklabels(
        my_xticks_labels,
        rotation=15,
        fontsize=12)
    # add legend
    ax_fairbox.legend(handles=[honest_node, fairline_PRA, fairline_PRV])
    pathlib.Path(draw_directory).mkdir(parents=True, exist_ok=True)
    logging.info("[qlep.draw_election_fair_boxplot] save figure START")
    figure_fairbox.savefig(
        draw_directory + '/fairboxplot.pdf',
        format='pdf',
        dpi=1200,
        bbox_inches='tight')
    plt.close(figure_fairbox)
    logging.info("[qlep.draw_election_fair_boxplot] end figure START")


def draw_stake_election_CDF(
        no_nodes: list[int] = [],
        election_types: list[qlep.core.ElectionType] = [],
        committee_types: list[qlep.core.CommitteeType] = [],
        providers: list[qlep.core.Provider] = [],
        backends: list[str] = [],
        simulate_directory: str = None,
        draw_directory: str = None
) -> None:
    r"""
    Draw the cumulative distribution function of the election results
    for the malicious winning percentage and the invalid elections
    percentage.

    Args:
        no_nodes :
            The list of the with number of nodes values to filter
            the quantum leader election protocols.
        election_types :
            The list of the election types to filter the quantum leader
            election protocols.
        committee_types :
            The list of the committee types to filter the quantum leader
            election protocols.
        providers :
            The list of the providers to filter the quantum leader
            election protocols.
        backends :
            The list of the backends to filter the quantum leader
            election protocols.
        simulate_directory :
            The directory where the simulation files are stored.
        draw_directory :
            The directory where the figures will be stored.
    """
    logging.info("[qlep.draw_stake_election_cdf] START")
    plt.rcParams['text.usetex'] = True
    plt.rcParams.update({'font.size': 22})
    # malicious winning percentage figure
    figure_stake_cdf, ax_stake_cdf = plt.subplots(figsize=(15, 15))

    logging.info("[qlep.draw_stake_election_cdf] initial axis setup START")
    # initial axis setup
    my_xlabel = r'share of stake'
    my_ylabel = r'share of elections/nodes'
    my_yticks = np.linspace(start=0, stop=1, num=11)
    my_xticks = np.linspace(start=0, stop=1, num=11)
    # setup x axis
    ax_stake_cdf.set_xlabel(my_xlabel)
    ax_stake_cdf.set_xticks(my_xticks)
    ax_stake_cdf.set_xlim(left=-0, right=1)
    # setup y axis
    ax_stake_cdf.set_ylabel(my_ylabel)
    ax_stake_cdf.set_yticks(my_yticks)
    ax_stake_cdf.set_ylim(bottom=-0, top=1)
    # grid
    ax_stake_cdf.grid(linestyle='--', axis='both')

    legendLines = []
    # add the legend lines
    nodes_legend_line = Line2D(
        [0],
        [0],
        color='k',
        ls='-.',
        lw=2,
        label=r'Share of nodes'
    )
    legendLines.append(nodes_legend_line)
    elections_legend_line = Line2D(
        [0],
        [0],
        color='k',
        ls='--',
        lw=2,
        label=r'Share of elections'
    )
    legendLines.append(elections_legend_line)
    fair_line = ax_stake_cdf.plot(
        [0, 1.0],
        [0, 1.0],
        color='k',
        linestyle='solid',
        label=r'Theoretical line of elections')
    legendLines.append(fair_line[0])
    logging.info("[qlep.draw_stake_election_cdf] initial axis setup END")

    # going through all the files in the directory
    logging.info("[qlep.draw_stake_election_cdf] pass through files START")
    qleps_with_data = get_filtered_qleps_with_data(
        no_nodes=no_nodes,
        election_types=election_types,
        committee_types=committee_types,
        providers=providers,
        backends=backends,
        simulate_directory=simulate_directory
    )
    logging.info("[qlep.draw_stake_election_cdf] pass through files END")
    for (current_qlep, analyse_results) in qleps_with_data:
        print(current_qlep.get_latex_name())
        if isinstance(
                current_qlep,
                qlep.core.QuantumLeaderElectionProtocolwithPoS):
            if current_qlep.use_stake is False:
                continue
            winning_percentages = analyse_results["winning_percentages"]
            no_nodes = len(winning_percentages[0])
            # the stake vector
            stake_vector = analyse_results["stake_vector"]
            total_stake = np.sum(stake_vector)
            stake_vector = stake_vector/total_stake

            zipped_list = list(zip(stake_vector, winning_percentages[0]))
            zipped_list.sort(key=lambda x: x[0])
            zipped_list[:0] = [(0, 0)]

            stake_cdf = [
                np.sum(
                    [z[0] for z in zipped_list[0:(index+1)]]
                )
                for index in range(no_nodes+1)
            ]
            win_cdf = [
                np.sum(
                    [z[1] for z in zipped_list[0:(index+1)]]
                )
                for index in range(no_nodes+1)
            ]

            plot_style = current_qlep.get_plot_style()
            plot_style['markersize'] = 0.5 * plot_style['markersize']
            ax_stake_cdf.plot(
                stake_cdf,
                win_cdf,
                alpha=0.6,
                **plot_style,
            )
            plot_style['linestyle'] = '-.'
            ax_stake_cdf.plot(
                stake_cdf,
                np.arange(no_nodes+1)/no_nodes,
                alpha=0.6,
                **plot_style,
            )
            plot_style = current_qlep.get_plot_style()
            plot_style['linestyle'] = ''
            legendLines.append(Line2D(
                [0],
                [0],
                **plot_style,
            ))
    # make the legend
    ax_stake_cdf.legend(
        handles=[x for x in legendLines],
        bbox_to_anchor=(1.04, 1),
        borderaxespad=0,
        loc="upper left")
    pathlib.Path(draw_directory).mkdir(parents=True, exist_ok=True)
    logging.info("[qlep.draw_stake_election_cdf] save figures START")
    figure_stake_cdf.savefig(
        draw_directory + '/stake_CDF.pdf',
        format='pdf',
        dpi=1200,
        bbox_inches='tight')
    plt.close(figure_stake_cdf)
    logging.info("[qlep.draw_stake_election_cdf] end figures START")


def draw_malicious_CDF(
        no_nodes: list[int] = [],
        election_types: list[qlep.core.ElectionType] = [],
        committee_types: list[qlep.core.CommitteeType] = [],
        providers: list[qlep.core.Provider] = [],
        backends: list[str] = [],
        simulate_directory: str = None,
        draw_directory: str = None
) -> None:
    r"""
    Draw the cumulative distribution function of the election results
    for the malicious winning percentage and the invalid elections
    percentage.

    Args:
        no_nodes :
            The list of the with number of nodes values to filter
            the quantum leader election protocols.
        election_types :
            The list of the election types to filter the quantum leader
            election protocols.
        committee_types :
            The list of the committee types to filter the quantum leader
            election protocols.
        providers :
            The list of the providers to filter the quantum leader
            election protocols.
        backends :
            The list of the backends to filter the quantum leader
            election protocols.
        simulate_directory :
            The directory where the simulation files are stored.
        draw_directory :
            The directory where the figures will be stored.
    """
    logging.info("[qlep.draw_malicious_CDF] START")
    plt.rcParams['text.usetex'] = True
    plt.rcParams.update({'font.size': 22})
    # malicious winning percentage figure
    figure_malicious_CDF, ax_malicious_CDF = plt.subplots(figsize=(15, 15))

    logging.info("[qlep.draw_malicious_CDF] initial axis setup START")
    my_xticks = [0, 0.5, 0.66, 1]
    my_xticks_labels = [r'0', r'$\frac{n}{4}$', r'$\frac{n}{3}$',
                        r'$\frac{n}{2}$']
    my_xlabel = r'Number of malicious nodes $ f = | \mathcal{M} | $'
    my_yticks = np.linspace(start=0, stop=1, num=11)
    # setup malicious labels
    ax_malicious_CDF.set_xlabel(my_xlabel)
    ax_malicious_CDF.set_xticks(ticks=my_xticks, labels=my_xticks_labels)
    ax_malicious_CDF.set_xlim(left=-0, right=1)
    ax_malicious_CDF.set_ylabel(r'Share of elections with malicious leader')
    ax_malicious_CDF.set_yticks(my_yticks)
    ax_malicious_CDF.set_ylim(bottom=-0, top=1)
    ax_malicious_CDF.grid(linestyle='--', axis='both')
    legendLines = []
    fair_line = ax_malicious_CDF.plot(
        [0, 1.0],
        [0, 0.5],
        color='black',
        linestyle='solid',
        lw=3,
        label=r'Theoretical Fair Line')
    legendLines.append(fair_line[0])
    logging.info("[qlep.draw_malicious_CDF] initial axis setup END")

    # going through all the files in the directory
    logging.info("[qlep.draw_malicious_CDF] pass through files START")
    qleps_with_data = get_filtered_qleps_with_data(
        no_nodes=no_nodes,
        election_types=election_types,
        committee_types=committee_types,
        providers=providers,
        backends=backends,
        simulate_directory=simulate_directory
    )
    for (current_qlep, analyse_results) in qleps_with_data:
        if isinstance(
                current_qlep,
                qlep.core.QuantumLeaderElectionProtocolwithPoS):
            if current_qlep.use_stake is True:
                continue
        print(current_qlep.get_latex_name())
        # find the maximum malicious
        max_no_malicious_nodes: int = analyse_results["max_no_malicious_nodes"]
        malicious_win_percentage = analyse_results["malicious_win_percentage"]
        plot_style = current_qlep.get_plot_style()
        # plot the malicious line
        malicious_plot_line = ax_malicious_CDF.plot(
            (
                np.arange(start=0, stop=max_no_malicious_nodes+1, step=1) /
                max_no_malicious_nodes
            ),
            malicious_win_percentage,
            alpha=0.6,
            **plot_style,
            # color='black'
        )
        # add to legend lines the current qlep
        legendLines.append(malicious_plot_line[0])
    # make the legend
    ax_malicious_CDF.legend(
        handles=[x for x in legendLines],
        bbox_to_anchor=(1.04, 1),
        borderaxespad=0,
        loc="upper left")
    pathlib.Path(draw_directory).mkdir(parents=True, exist_ok=True)
    logging.info("[qlep.draw_malicious_CDF] save figures START")
    figure_malicious_CDF.savefig(
        draw_directory + '/malicious_CDF.pdf',
        format='pdf',
        dpi=1200,
        bbox_inches='tight')
    plt.close(figure_malicious_CDF)
    logging.info("[qlep.draw_malicious_CDF] end figures START")
