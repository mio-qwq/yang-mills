# Independent audit: finite torus diagonal reflection obstruction

## Conclusion and scope
The proposed coefficient is correct for the Gibbs density exp(beta sum_p X_p), with X_p=(1/2)Tr U_p, on a fixed four-dimensional periodic lattice of side n>=8. For the coordinate-swap involution theta and positive algebra containing all (2,3)-plaquettes with representatives x0>x1, the proposed F=P-Q has reflected squared form

E_beta[(theta F) F] = -beta^4/512 + O_n(beta^5).

It is strictly negative for sufficiently small positive beta (the neighborhood may depend on n). This disproves this precise finite-volume reflection-positivity assertion. It does not establish any failure of continuum reflection positivity or any Yang–Mills existence statement. The selected torus half is not a geometrically separating reflection half.

## Conventions
Use normalized independent SU(2) Haar edge variables. Plaquettes are unoriented geometric squares, represented by base x and ordered directions i<j. Reversing a plaquette orientation leaves its real SU(2) trace unchanged. Let theta swap coordinates 0 and 1 and act by pullback and complex conjugation on functions. The functions used below are real, so conjugation is inert.

If instead the action is beta sum Tr U_p, the numerical coefficient changes by 2^4. The sign does not change. The following coefficient presumes normalized trace couplings.

## Peeling lemma and repeated indices
Given a set S of distinct plaquettes, suppose p has an edge absent from every other plaquette of S. Conditional on all other edge variables, U_p is a fixed left/right translate of that independent Haar edge or its inverse. Consequently X_p has its one-plaquette Haar law and is independent of the whole random vector (X_q:q in S minus p). This statement holds for arbitrary powers, not merely first moments.

Iteratively remove such p. If S peels completely, its trace variables are independent. Therefore every mixed cumulant supported on S vanishes, including cumulants with repeated plaquette indices. More generally, an exposed variable is independent of all the others and any mixed cumulant involving it vanishes. Thus a possibly nonzero mixed cumulant has a nonempty non-peelable support. At total degree <=6, support has at most six distinct plaquettes.

## Exhaustive small-core classification
Distinct plaquettes on the n>=8 torus share at most one edge. In a non-peelable support containing a root square, each of its four edges requires a different neighboring square. There must therefore be at least five distinct squares. For support of size at most six, choose one neighbor at each root edge, giving root plus four squares. Each root edge has exactly five alternative incident plaquettes in four dimensions, so there are 5^4=625 choices.

For each such five-square set, compute the singly covered boundary edges. If none exist, it is already a core. Otherwise the only possible sixth square must contain EVERY such boundary edge. Intersect their incident-square sets and test every candidate. This exhausts even disconnected candidates: a core component containing the root already needs at least five faces; another core cannot fit in the six-face budget.

Independent code audit.py implements this exhaustive method directly modulo 8 for all six root orientations. It finds zero five-square cores and exactly four six-square cores for each root orientation, precisely the elementary cube boundaries through that square. This does not rely on the discoverer's code or its output.

The same combinatorial certificate applies to all n>=8. Every chosen neighboring square admits the usual local integer lift around the root. Its edges lie in a bounded coordinate box near the root. Any proposed sixth square is incident to an edge of that five-square set, so its coordinates also lie within this local box expanded by one lattice unit. No pair of these local vertices separated by n>=8 can coincide. Thus the local incidence tests agree with the integer lattice and are independent of torus side length. In particular, there are no small wrapping cores accidentally omitted by using n=8.

## Haar cube integral
For an elementary cube surface, orient its six faces outward. Each link appears once in each direction. Gauge-fix any spanning tree of its eight vertices (seven links). Haar gauge invariance preserves the remaining independent Haar integrals. The five unfixed links correspond to a dual spanning tree among the six faces. Integrating these links successively merges adjacent face characters using

integral Tr(AU) Tr(U^{-1}B) dU = Tr(AB)/2.

After five merges the remaining boundary word is trivial, giving Tr(I)=2. Hence the product of six UNnormalized fundamental characters has integral 2*(1/2)^5=1/16. Six normalized traces supply the additional factor 2^-6, giving 1/1024.

Every proper subset of cube faces peels completely and has independent zero-mean normalized traces. Therefore the six-distinct-variable joint cumulant equals the full cube moment, 1/1024. No disconnected partition survives.

## Partition function and factorials
Introduce independent plaquette couplings t_p and Z(t)=E_Haar exp(sum_p t_p X_p). Up to total degree six,

log Z(t) = sum_p log z(t_p) + (1/1024) sum_elementary_cubes product_faces_of_cube t_p + O(total degree 7),

where z(t)=E_Haar exp(t X). The peeling argument gives exact cancellation for every repeated-index mixed cumulant. At degree six the only possible non-peelable support is a cube, with all six indices distinct. Its multivariate monomial has coefficient equal to its joint cumulant: the six factorial permutations cancel the exponential-series 6! denominator. No extra combinatorial factor belongs in the displayed cube sum.

For two distinct plaquettes a,b, differentiating twice and setting all t_p=beta gives

Cov_beta(X_a,X_b) = N(a,b)*beta^4/1024 + O_n(beta^5),

where N counts elementary cubes containing both.

## Geometry and sign
Set all unspecified base coordinates to zero. P is the (2,3) plaquette at (n-1,2), Q the (2,3) plaquette at (2,0). Both are nonwrapping contractible plaquettes contained in the prescribed representative half x0>x1. Their images have bases theta P=(2,n-1), theta Q=(0,2).

The pair (P,theta Q) is the pair of opposite (2,3) faces of exactly one cube in directions (0,2,3) crossing the periodic 0-boundary. Likewise (Q,theta P) belongs to exactly one (1,2,3) cube across the periodic 1-boundary. Neither (P,theta P) nor (Q,theta Q) belongs to a common elementary cube. All four plaquettes are distinct for n>=8.

Thus the cube-count matrix in the ordered basis (P,Q) is [[0,1],[1,0]]. F=P-Q has coefficient (1,-1)M(1,-1)^T/1024 = -2/1024 = -1/512. Translation invariance gives E_beta P=E_beta Q exactly, so E_beta F=0; centering adds no qualification. Reflection invariance gives the same for theta F.

## Analytic remainder
The finite lattice has finitely many compact SU(2) edge integrals and |X_p|<=1. Its multivariate Z is entire, Z(0)=1, and has a nonvanishing complex neighborhood of zero. A local analytic logarithm therefore exists. The Taylor remainder after degree six, differentiated twice and restricted to t_p=beta, is O_n(beta^5). Equivalently, the reflected form is a real-analytic function near beta=0 with first nonzero coefficient -1/512 at order four. There is consequently some epsilon_n>0 for which it is negative throughout 0<beta<epsilon_n. No volume-uniform estimate is claimed.

## Explicit rational small-beta range (independent check of root proposal)
Let M=6n^4 be the number of geometric plaquettes and S=sum_p X_p. Let G=F(theta F). Then |G|<=4 and |S|<=M. The unnormalized numerator N(beta)=E_Haar[G exp(beta S)] has Taylor coefficients zero through degree three and coefficient -1/512 at degree four, since N=Z E_beta G and Z(0)=1. Consequently

|N(beta)+beta^4/512| <= 4 exp(beta M) (beta M)^5/120.

For every 0<beta<=1/(128 M^5), beta M<=1/128 and exp(beta M)<=1/(1-beta M)<=128/127. Dividing the bound by beta^4 gives at most

exp(beta M) beta M^5/30 <= 1/3810 < 1/1024.

Thus N(beta)<=-beta^4/1024<0 throughout this explicit rational range. Z(beta)>0 because its integrand is strictly positive. In particular beta=1/[128(6n^4)^5] is a concrete parameter witnessing failure. This strengthens the analytic existence argument without claiming an optimal range.
