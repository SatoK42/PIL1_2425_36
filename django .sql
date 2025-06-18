-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 18 juin 2025 à 21:50
-- Version du serveur : 9.1.0
-- Version de PHP : 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `django`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_app_users`
--

DROP TABLE IF EXISTS `auth_app_users`;
CREATE TABLE IF NOT EXISTS `auth_app_users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(191) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phone_number` varchar(128) NOT NULL,
  `role` varchar(20) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone_number` (`phone_number`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_app_users`
--

INSERT INTO `auth_app_users` (`id`, `email`, `first_name`, `last_name`, `password`, `phone_number`, `role`, `date_joined`, `is_active`, `is_staff`, `is_superuser`, `last_login`) VALUES
(1, 'oswaldkagbahinto@gmail.com', 'MK', 'faith', 'pbkdf2_sha256$1000000$FvDRHTacHDTWn66P0ekOaV$IIgCNFnmrKPz9GQvI4M9JJPuXTfFVubjo3EfJndddTo=', '+22991862280', 'conducteur', '2025-06-13 19:20:46.457026', 1, 0, 0, '2025-06-16 09:14:06.902154'),
(2, 'faithank15@gmail.com', 'AZ', 'Rocky', 'pbkdf2_sha256$1000000$gpUCXbaVxzaX1unociEDru$j974pOSE2UEGtsDW2wiVn1MOUABY5WenuDPOKGkdKK8=', '+22996000000', 'conducteur', '2025-06-13 19:34:44.972704', 1, 0, 0, '2025-06-18 13:52:31.629373'),
(3, 'tony@gmail.com', 'STARK', 'Tony', 'pbkdf2_sha256$1000000$wwtJ2dMczs1HByB89oGWcp$RUHvZIuG/E9iEwG97+bOi6OP0cWI6icpU946cxqKW60=', '+22991919191', 'conducteur', '2025-06-16 14:15:56.864675', 1, 0, 0, '2025-06-17 17:28:21.547721'),
(4, 'MAN@gmail.com', 'IRON', 'MAN', 'pbkdf2_sha256$1000000$Kqti9qlbotPUPnOLx6qIWI$Sggwkh2lJfbnGNTisz8VVjk4Tqko/gRskcF2gfqq46w=', '+22996969696', 'conducteur', '2025-06-16 20:51:17.156508', 1, 0, 0, '2025-06-16 20:55:57.306709'),
(5, 'anthe@gmail.com', 'Anthe', 'MAN', 'pbkdf2_sha256$1000000$h4fOogjIAr48ijjyMbvEpt$E0LqWYNoFgo0kM9xhDqn3fJmjdF9PJ511w9+YLPAYS4=', '+22995959595', 'conducteur', '2025-06-16 20:58:56.024339', 1, 0, 0, '2025-06-16 20:59:19.944978'),
(6, 'hulk@gmail.com', 'Mr', 'Hulk', 'pbkdf2_sha256$1000000$3lwtVs3z2iQtB0Qeuo0gC1$WFQU/BmctYcUCMH5qusDGK5S9QzvcCHPaaVrCMNiyGk=', '+22997979797', 'passager', '2025-06-18 13:38:23.186742', 1, 0, 0, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `auth_app_users_groups`
--

DROP TABLE IF EXISTS `auth_app_users_groups`;
CREATE TABLE IF NOT EXISTS `auth_app_users_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `users_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_app_users_groups_users_id_group_id_f4b15007_uniq` (`users_id`,`group_id`),
  KEY `auth_app_users_groups_users_id_e4f1fca5` (`users_id`),
  KEY `auth_app_users_groups_group_id_9037f558` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_app_users_user_permissions`
--

DROP TABLE IF EXISTS `auth_app_users_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_app_users_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `users_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_app_users_user_perm_users_id_permission_id_41284ed0_uniq` (`users_id`,`permission_id`),
  KEY `auth_app_users_user_permissions_users_id_cc035993` (`users_id`),
  KEY `auth_app_users_user_permissions_permission_id_0d522746` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add users', 7, 'add_users'),
(26, 'Can change users', 7, 'change_users'),
(27, 'Can delete users', 7, 'delete_users'),
(28, 'Can view users', 7, 'view_users'),
(29, 'Can add conversation', 8, 'add_conversation'),
(30, 'Can change conversation', 8, 'change_conversation'),
(31, 'Can delete conversation', 8, 'delete_conversation'),
(32, 'Can view conversation', 8, 'view_conversation'),
(33, 'Can add conversation user', 9, 'add_conversationuser'),
(34, 'Can change conversation user', 9, 'change_conversationuser'),
(35, 'Can delete conversation user', 9, 'delete_conversationuser'),
(36, 'Can view conversation user', 9, 'view_conversationuser'),
(37, 'Can add message', 10, 'add_message'),
(38, 'Can change message', 10, 'change_message'),
(39, 'Can delete message', 10, 'delete_message'),
(40, 'Can view message', 10, 'view_message'),
(41, 'Can add trajet', 11, 'add_trajet'),
(42, 'Can change trajet', 11, 'change_trajet'),
(43, 'Can delete trajet', 11, 'delete_trajet'),
(44, 'Can view trajet', 11, 'view_trajet'),
(45, 'Can add chat', 12, 'add_chat'),
(46, 'Can change chat', 12, 'change_chat'),
(47, 'Can delete chat', 12, 'delete_chat'),
(48, 'Can view chat', 12, 'view_chat'),
(49, 'Can add attachment', 13, 'add_attachment'),
(50, 'Can change attachment', 13, 'change_attachment'),
(51, 'Can delete attachment', 13, 'delete_attachment'),
(52, 'Can view attachment', 13, 'view_attachment'),
(53, 'Can add conversation', 14, 'add_conversation'),
(54, 'Can change conversation', 14, 'change_conversation'),
(55, 'Can delete conversation', 14, 'delete_conversation'),
(56, 'Can view conversation', 14, 'view_conversation'),
(57, 'Can add message', 15, 'add_message'),
(58, 'Can change message', 15, 'change_message'),
(59, 'Can delete message', 15, 'delete_message'),
(60, 'Can view message', 15, 'view_message'),
(61, 'Can add profile', 16, 'add_profile'),
(62, 'Can change profile', 16, 'change_profile'),
(63, 'Can delete profile', 16, 'delete_profile'),
(64, 'Can view profile', 16, 'view_profile'),
(65, 'Can add matching', 17, 'add_matching'),
(66, 'Can change matching', 17, 'change_matching'),
(67, 'Can delete matching', 17, 'delete_matching'),
(68, 'Can view matching', 17, 'view_matching'),
(69, 'Can add notification', 18, 'add_notification'),
(70, 'Can change notification', 18, 'change_notification'),
(71, 'Can delete notification', 18, 'delete_notification'),
(72, 'Can view notification', 18, 'view_notification'),
(73, 'Can add match', 19, 'add_match'),
(74, 'Can change match', 19, 'change_match'),
(75, 'Can delete match', 19, 'delete_match'),
(76, 'Can view match', 19, 'view_match');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$1000000$S1QolZy71smuQ2kL5yIOkT$LTeYqJo/gj/G5iPtH5UilfHU8f6itgd7ocemwQN+/TI=', '2025-06-13 15:32:49.277229', 1, 'IFRI', '', '', '', 1, 1, '2025-06-09 13:31:41.856733');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'auth_app', 'users'),
(8, 'messagerie', 'conversation'),
(9, 'messagerie', 'conversationuser'),
(10, 'messagerie', 'message'),
(11, 'trajet', 'trajet'),
(12, 'messagerie', 'chat'),
(13, 'messagerie', 'attachment'),
(14, 'messaging_app', 'conversation'),
(15, 'messaging_app', 'message'),
(16, 'profileUser', 'profile'),
(17, 'trajet', 'matching'),
(18, 'trajet', 'notification'),
(19, 'trajet', 'match');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-06-09 13:23:12.738496'),
(2, 'auth', '0001_initial', '2025-06-09 13:23:13.816908'),
(3, 'admin', '0001_initial', '2025-06-09 13:23:13.960184'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-06-09 13:23:13.964494'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-06-09 13:23:13.968928'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-06-09 13:23:14.040409'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-06-09 13:23:14.080573'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-06-09 13:23:14.112507'),
(9, 'auth', '0004_alter_user_username_opts', '2025-06-09 13:23:14.121193'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-06-09 13:23:14.159781'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-06-09 13:23:14.161133'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-06-09 13:23:14.166170'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-06-09 13:23:14.197591'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-06-09 13:23:14.236799'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-06-09 13:23:14.267828'),
(16, 'auth', '0011_update_proxy_permissions', '2025-06-09 13:23:14.274354'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-06-09 13:23:14.304205'),
(18, 'auth_app', '0001_initial', '2025-06-09 13:23:14.312659'),
(19, 'sessions', '0001_initial', '2025-06-09 13:23:14.350003'),
(20, 'auth_app', '0002_remove_users_first_name_remove_users_last_name_and_more', '2025-06-13 08:20:39.019425'),
(29, 'messagerie', '0001_initial', '2025-06-14 05:55:48.513624'),
(22, 'trajet', '0001_initial', '2025-06-13 08:20:39.636172'),
(23, 'auth_app', '0003_users_email_users_first_name_users_last_name_and_more', '2025-06-13 15:04:13.954506'),
(24, 'auth_app', '0004_alter_users_options_alter_users_managers_and_more', '2025-06-13 19:20:25.936295'),
(30, 'messagerie', '0002_alter_conversation_participants_and_more', '2025-06-14 05:55:48.527384'),
(26, 'trajet', '0002_alter_trajet_user', '2025-06-13 19:20:25.965127'),
(27, 'auth_app', '0005_remove_users_username_alter_users_email', '2025-06-13 19:33:23.148181'),
(28, 'auth_app', '0006_alter_users_email', '2025-06-13 19:33:28.646448'),
(31, 'messagerie', '0002_remove_chat_participants_remove_message_chat_and_more', '2025-06-14 07:01:26.855632'),
(32, 'messaging_app', '0001_initial', '2025-06-14 07:46:40.222104'),
(33, 'profileUser', '0001_initial', '2025-06-15 13:42:52.735508'),
(34, 'profileUser', '0002_alter_profil_user', '2025-06-15 13:42:52.742335'),
(35, 'profileUser', '0003_rename_profil_profile', '2025-06-15 13:42:52.768275'),
(36, 'profileUser', '0004_remove_profile_quartier_remove_profile_ville_and_more', '2025-06-15 17:40:37.952072'),
(37, 'trajet', '0002_add_notification_table', '2025-06-17 15:09:59.711407');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('uwprgf101ux68jpyq6jxzuw40hpjqxon', '.eJxVyzsOwjAQRdG9uEaRv2ObEik12YE1Ho_kCAhRTKqIvfNRCmjPe3cTCddHTWvjJY1FHIURh1_LSBeePsPXcJ67nVrX33C8npeh3ic-7b-_uGKr79KCJrCuoMQSQNriZFTasEEIBCorZaXORIYcowHIHqKXHGLUbL0i8XwB0gM1mg:1uRa6f:YLWckfJUTMGYYtOGyaTc4jSXeggu3kbLn5i_w2HTpIg', '2025-07-01 17:28:21.554945'),
('l28fzyb6z1lkt73k3uz8eno4q7mhwrza', '.eJxVyzsOwjAQhOG7uEaRdzMmgRKJGm5g7caLHAEhikmFuDsPpYD2m_kfLsp8z3EuNsU-ua1jt_o1le5sw2f4moxjtVCp9lfpL4fpmG-D7ZbfX5yl5HcJgQfQMhTaSRIK6w2j9h41cCKjkFQaalkhDLCn0KSg5skLk7nnC8I3NTY:1uRtDL:PCkR9VrHueKmDhW_8oJhFTunzoDh45g_AO2Kec4TJR8', '2025-07-02 13:52:31.636153');

-- --------------------------------------------------------

--
-- Structure de la table `messagerie_conversation`
--

DROP TABLE IF EXISTS `messagerie_conversation`;
CREATE TABLE IF NOT EXISTS `messagerie_conversation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_creation` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `messagerie_conversationuser`
--

DROP TABLE IF EXISTS `messagerie_conversationuser`;
CREATE TABLE IF NOT EXISTS `messagerie_conversationuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `messagerie_message`
--

DROP TABLE IF EXISTS `messagerie_message`;
CREATE TABLE IF NOT EXISTS `messagerie_message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `messaging_app_conversation`
--

DROP TABLE IF EXISTS `messaging_app_conversation`;
CREATE TABLE IF NOT EXISTS `messaging_app_conversation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_group` tinyint(1) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `messaging_app_conversation`
--

INSERT INTO `messaging_app_conversation` (`id`, `is_group`, `name`, `created_at`) VALUES
(1, 0, 'MK', '2025-06-14 07:48:30.762457'),
(2, 0, 'AZ', '2025-06-14 07:49:00.153235'),
(3, 0, NULL, '2025-06-14 08:02:57.985856'),
(4, 0, NULL, '2025-06-14 08:09:27.808789'),
(5, 0, 'Group1', '2025-06-14 08:18:04.967825'),
(6, 0, NULL, '2025-06-14 19:55:56.017713'),
(7, 0, NULL, '2025-06-14 21:08:50.752308'),
(8, 0, NULL, '2025-06-14 23:27:16.945974'),
(9, 1, 'Group1', '2025-06-14 23:31:48.975264'),
(10, 1, 'Group2', '2025-06-14 23:37:10.742501'),
(11, 0, NULL, '2025-06-14 23:39:04.284454'),
(12, 0, NULL, '2025-06-14 23:43:43.112093'),
(13, 0, NULL, '2025-06-14 23:44:56.874654'),
(14, 0, NULL, '2025-06-15 08:37:41.335997'),
(15, 0, NULL, '2025-06-15 08:38:00.980790'),
(16, 0, NULL, '2025-06-15 08:39:47.079101'),
(17, 0, NULL, '2025-06-15 11:13:30.896327'),
(18, 0, NULL, '2025-06-15 11:13:42.403633'),
(19, 0, NULL, '2025-06-15 11:23:11.270690'),
(20, 0, NULL, '2025-06-16 06:36:54.513070'),
(21, 0, NULL, '2025-06-17 20:46:24.736824'),
(22, 0, NULL, '2025-06-18 18:07:05.409471');

-- --------------------------------------------------------

--
-- Structure de la table `messaging_app_conversation_participants`
--

DROP TABLE IF EXISTS `messaging_app_conversation_participants`;
CREATE TABLE IF NOT EXISTS `messaging_app_conversation_participants` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `conversation_id` bigint NOT NULL,
  `users_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `messaging_app_conversati_conversation_id_users_id_497e2455_uniq` (`conversation_id`,`users_id`),
  KEY `messaging_app_conversation_participants_conversation_id_36d6a6cd` (`conversation_id`),
  KEY `messaging_app_conversation_participants_users_id_738ca0f4` (`users_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `messaging_app_conversation_participants`
--

INSERT INTO `messaging_app_conversation_participants` (`id`, `conversation_id`, `users_id`) VALUES
(1, 4, 2),
(2, 5, 1),
(3, 6, 1),
(4, 7, 1),
(5, 8, 1),
(6, 9, 2),
(7, 10, 2),
(8, 11, 1),
(9, 12, 1),
(10, 13, 2),
(11, 14, 2),
(12, 15, 2),
(13, 16, 1),
(14, 17, 1),
(15, 17, 2),
(16, 18, 1),
(17, 19, 1),
(18, 20, 1),
(19, 20, 2),
(20, 21, 2),
(21, 21, 3),
(22, 22, 2),
(23, 22, 6);

-- --------------------------------------------------------

--
-- Structure de la table `messaging_app_message`
--

DROP TABLE IF EXISTS `messaging_app_message`;
CREATE TABLE IF NOT EXISTS `messaging_app_message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext,
  `image` varchar(100) DEFAULT NULL,
  `audio` varchar(100) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `conversation_id` bigint NOT NULL,
  `sender_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `messaging_app_message_conversation_id_64db5655` (`conversation_id`),
  KEY `messaging_app_message_sender_id_b4ab2604` (`sender_id`)
) ENGINE=MyISAM AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `messaging_app_message`
--

INSERT INTO `messaging_app_message` (`id`, `text`, `image`, `audio`, `timestamp`, `conversation_id`, `sender_id`) VALUES
(1, 'yo', '', '', '2025-06-14 21:07:48.816572', 6, 1),
(2, 'yo', '', '', '2025-06-14 21:08:55.267325', 7, 1),
(3, 'yo', '', '', '2025-06-14 21:09:24.184688', 5, 1),
(4, 'comment ca va?', '', '', '2025-06-14 21:09:39.518412', 5, 1),
(5, 'Hello', '', '', '2025-06-14 21:10:11.641482', 5, 1),
(6, 'c\'est comment vieux?', '', '', '2025-06-14 21:10:21.292839', 5, 1),
(7, 'yo\n', '', '', '2025-06-14 23:29:10.542004', 8, 1),
(8, 'yo\n', '', '', '2025-06-14 23:31:55.256565', 9, 2),
(9, 'cc\n', '', '', '2025-06-14 23:32:23.518427', 9, 2),
(10, 'yo', '', '', '2025-06-14 23:32:58.020625', 9, 2),
(11, 'cc', '', '', '2025-06-14 23:33:02.883045', 9, 2),
(12, 'cc', '', '', '2025-06-14 23:33:08.123145', 9, 2),
(13, 'cc', '', '', '2025-06-14 23:33:11.998677', 9, 2),
(14, 'cc', '', '', '2025-06-14 23:33:21.571086', 9, 2),
(15, 'yo', '', '', '2025-06-14 23:33:25.158021', 9, 2),
(16, 'ygy', '', '', '2025-06-14 23:33:53.998482', 9, 2),
(17, 'h', '', '', '2025-06-14 23:36:23.238092', 9, 2),
(18, 'h', '', '', '2025-06-14 23:36:30.709927', 9, 2),
(19, 'v\n', '', '', '2025-06-14 23:36:38.178813', 9, 2),
(20, 'j\n', '', '', '2025-06-14 23:36:45.654128', 9, 2),
(21, 'yo\n', '', '', '2025-06-14 23:37:15.532305', 10, 2),
(22, 'cc', '', '', '2025-06-14 23:39:07.887250', 11, 1),
(23, 'cc', '', '', '2025-06-14 23:39:29.359318', 11, 1),
(24, 'yo\n', '', '', '2025-06-14 23:39:36.110554', 11, 1),
(25, 'yo', '', '', '2025-06-14 23:43:47.533798', 12, 1),
(26, 'slt\n', '', '', '2025-06-14 23:44:03.299036', 12, 1),
(27, 'cc', '', '', '2025-06-14 23:45:03.736749', 13, 2),
(28, 'yo\n', '', '', '2025-06-14 23:45:21.382434', 13, 2),
(29, 'slt\n', '', '', '2025-06-14 23:45:37.453881', 13, 2),
(30, 'slt\n', '', '', '2025-06-14 23:45:45.346211', 13, 2),
(31, 'yo', '', '', '2025-06-15 08:37:45.561727', 14, 2),
(32, 'yo', '', '', '2025-06-15 08:38:10.695578', 15, 2),
(33, 'sla', '', '', '2025-06-15 08:39:02.993882', 15, 2),
(34, 'sla', '', '', '2025-06-15 08:39:32.177865', 15, 2),
(35, 'yo', '', '', '2025-06-15 08:39:50.903191', 16, 1),
(36, 'salut', '', '', '2025-06-15 08:39:55.510957', 16, 1),
(37, 'yo', '', '', '2025-06-15 11:23:15.346400', 19, 1),
(38, 'slt', '', '', '2025-06-15 11:23:19.331688', 19, 1),
(39, 'yo\n', '', '', '2025-06-15 11:37:43.787341', 19, 1),
(40, 'comment ca va\n', '', '', '2025-06-15 11:37:51.130337', 19, 1),
(41, 'tre', '', '', '2025-06-15 11:38:04.778254', 19, 1),
(42, 'yo\n', '', '', '2025-06-15 13:44:00.687074', 17, 1),
(43, 'ca va?\n', '', '', '2025-06-15 13:44:08.744098', 17, 1),
(44, 'moi je vais bien', '', '', '2025-06-15 13:44:22.812665', 17, 1),
(45, 'ok c\'est cool', '', '', '2025-06-15 13:44:52.121640', 17, 2),
(46, 'Et la famille?\n', '', '', '2025-06-15 14:04:01.207588', 17, 2),
(47, 'Ca va?', '', '', '2025-06-15 14:04:10.961803', 17, 2),
(48, 'A', '', '', '2025-06-15 14:04:30.776042', 17, 2),
(49, 'B', '', '', '2025-06-15 14:04:34.080007', 17, 2),
(50, 'C', '', '', '2025-06-15 14:04:40.237845', 17, 2),
(51, 'yo\n', '', '', '2025-06-15 15:45:34.441798', 17, 2),
(52, 'A\n', '', '', '2025-06-15 15:45:56.235198', 17, 2),
(53, 'Z', '', '', '2025-06-15 15:46:01.981388', 17, 2),
(54, 'cc', '', '', '2025-06-16 05:15:21.291197', 17, 2),
(55, 'zut', '', '', '2025-06-16 05:15:28.911878', 17, 2),
(56, 'ça marche?', '', '', '2025-06-16 05:18:57.278886', 17, 2),
(57, 'ok', '', '', '2025-06-16 05:20:03.421047', 17, 2),
(58, 'et?', '', '', '2025-06-16 05:20:12.655816', 17, 2),
(59, 'bon?', '', '', '2025-06-16 05:21:23.839183', 17, 2),
(60, 'ok?', '', '', '2025-06-16 05:27:33.483889', 17, 2),
(61, 'cool', '', '', '2025-06-16 05:27:42.252756', 17, 2),
(62, '1235', '', '', '2025-06-16 05:32:43.506195', 17, 2),
(63, 'd\'acc', '', '', '2025-06-16 05:32:51.508199', 17, 2),
(64, 'la c\'est bon', '', '', '2025-06-16 05:33:00.681702', 17, 2),
(65, 'slt', '', '', '2025-06-16 06:36:59.457732', 20, 2),
(66, 'yo\n', '', '', '2025-06-17 10:12:42.256709', 20, 2),
(67, 'ca va?\n', '', '', '2025-06-17 10:12:49.438896', 20, 2),
(68, 'Salut ça va?', '', '', '2025-06-17 20:46:34.590699', 21, 2),
(69, 'oui et toi?', '', '', '2025-06-17 20:46:52.960592', 21, 3),
(70, 'Ca va', '', '', '2025-06-17 20:47:00.150425', 21, 2),
(71, 'Cool', '', '', '2025-06-17 20:54:11.392192', 21, 3),
(72, 'Ok ndk?', '', '', '2025-06-17 20:54:21.726509', 21, 2);

-- --------------------------------------------------------

--
-- Structure de la table `profileuser_profile`
--

DROP TABLE IF EXISTS `profileuser_profile`;
CREATE TABLE IF NOT EXISTS `profileuser_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `photo` varchar(100) DEFAULT NULL,
  `user_id` bigint NOT NULL,
  `brand` varchar(100) DEFAULT NULL,
  `departure_lat` double DEFAULT NULL,
  `departure_lng` double DEFAULT NULL,
  `departure_time` time(6) DEFAULT NULL,
  `is_driver` tinyint(1) NOT NULL,
  `model` varchar(100) DEFAULT NULL,
  `seats` int UNSIGNED DEFAULT NULL,
  `vehicle_type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ;

--
-- Déchargement des données de la table `profileuser_profile`
--

INSERT INTO `profileuser_profile` (`id`, `photo`, `user_id`, `brand`, `departure_lat`, `departure_lng`, `departure_time`, `is_driver`, `model`, `seats`, `vehicle_type`) VALUES
(1, 'photos/img.jpg', 2, 'Wave', 6.453851, 2.33883, '06:15:00.000000', 1, '250', 1, 'moto'),
(2, 'photos/417439640_122173877264075374_3607579750964158292_n.jpg', 3, '', 6.454495, 2.334919, '06:20:00.000000', 0, '', NULL, NULL),
(3, '', 4, '', NULL, NULL, NULL, 0, '', NULL, NULL),
(4, '', 5, 'Wave', NULL, NULL, NULL, 1, '250', 1, 'moto'),
(5, '', 6, '', NULL, NULL, NULL, 0, '', NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `trajet_match`
--

DROP TABLE IF EXISTS `trajet_match`;
CREATE TABLE IF NOT EXISTS `trajet_match` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_accepted` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `demande_id` bigint NOT NULL,
  `offre_id` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `trajet_match`
--

INSERT INTO `trajet_match` (`id`, `is_accepted`, `created_at`, `demande_id`, `offre_id`) VALUES
(1, 0, '2025-06-18 06:24:05.737172', 1, 2),
(2, 0, '2025-06-18 07:22:13.947330', 4, 3);

-- --------------------------------------------------------

--
-- Structure de la table `trajet_notification`
--

DROP TABLE IF EXISTS `trajet_notification`;
CREATE TABLE IF NOT EXISTS `trajet_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `trajet_notification_user_id_248968e1` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `trajet_notification`
--

INSERT INTO `trajet_notification` (`id`, `message`, `is_read`, `created_at`, `user_id`) VALUES
(1, 'Nouvelle correspondance avec AZ Rocky pour le trajet #2.', 1, '2025-06-18 06:23:59.176811', 3),
(2, 'None a accepté le trajet (Match #1).', 1, '2025-06-18 06:24:05.755849', 3),
(3, 'Nouvelle correspondance avec STARK Tony pour le trajet #4.', 0, '2025-06-18 07:22:04.259174', 2),
(4, 'None a accepté le trajet (Match #2).', 0, '2025-06-18 07:22:13.962536', 2);

-- --------------------------------------------------------

--
-- Structure de la table `trajet_trajet`
--

DROP TABLE IF EXISTS `trajet_trajet`;
CREATE TABLE IF NOT EXISTS `trajet_trajet` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `role` varchar(20) NOT NULL,
  `lieu_depart` varchar(150) NOT NULL,
  `lieu_arrivee` varchar(150) NOT NULL,
  `latitude_depart` double NOT NULL,
  `longitude_depart` double NOT NULL,
  `heure` time(6) NOT NULL,
  `nb_places` int UNSIGNED DEFAULT NULL,
  `commentaire` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `date` date DEFAULT NULL,
  `latitude_arrivee` double NOT NULL,
  `longitude_arrivee` double NOT NULL,
  `recurring` tinyint(1) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `trajet_trajet_user_id_b222e47a` (`user_id`)
) ;

--
-- Déchargement des données de la table `trajet_trajet`
--

INSERT INTO `trajet_trajet` (`id`, `role`, `lieu_depart`, `lieu_arrivee`, `latitude_depart`, `longitude_depart`, `heure`, `nb_places`, `commentaire`, `created_at`, `user_id`, `date`, `latitude_arrivee`, `longitude_arrivee`, `recurring`, `status`) VALUES
(1, 'passager', 'Coordonnées sélectionnées', 'IFRI UAC', 6.45369355148947, 2.3379396474774694, '06:20:00.000000', NULL, '', '2025-06-18 06:22:33.038216', 3, '2025-06-19', 2.340447, 6.416676, 0, 'matched'),
(2, 'conducteur', 'Coordonnées sélectionnées', 'IFRI UAC', 6.453825882724966, 2.338846206498602, '06:14:00.000000', 1, '', '2025-06-18 06:23:59.158522', 2, '2025-06-19', 2.340447, 6.416676, 0, 'matched'),
(3, 'conducteur', 'Point habituel', 'IFRI UAC', 6.453851, 2.33883, '06:15:00.000000', 1, '', '2025-06-18 07:21:16.576776', 2, NULL, 2.340447, 6.416676, 1, 'matched'),
(4, 'passager', 'Point habituel', 'IFRI UAC', 6.454495, 2.334919, '06:20:00.000000', NULL, '', '2025-06-18 07:22:04.237877', 3, NULL, 2.340447, 6.416676, 1, 'matched');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
